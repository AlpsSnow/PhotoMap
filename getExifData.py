#!/usr/bin/env python
# coding: utf-8


"""
   getExifData.py,批量取一个文件夹下照片的坐标，日期，照片名字
"""

import exifread
import os

#提取照片坐标和拍摄时间
def extractExif(fpath):    
    try:
        with open(fpath,'rb') as rf:
            exif=exifread.process_file(rf)
        eDate=exif['EXIF DateTimeOriginal'].printable
        eLon=exif['GPS GPSLongitude'].printable
        eLat=exif['GPS GPSLatitude'].printable

        #'[116, 29, 10533/500]' to [116,29,10533,500]  type==(list)
        lon=eLon[1:-1].replace(' ','').replace('/',',').split(',') 
        #经度     
        lon=float(lon[0])+float(lon[1])/60+float(lon[2])/float(lon[3])/3600

        lat=eLat[1:-1].replace(' ','').replace('/',',').split(',')
        lat=float(lat[0])+float(lat[1])/60+float(lat[2])/float(lat[3])/3600

        p = fpath.rfind('/',0,len(fpath))
        f = fpath[p+1:len(fpath)]

        return [f,eDate,lon,lat]  #照片的名字,拍摄时间,经度,纬度
    except Exception as e:
        print(e,fpath)
        return None

#批量取一个文件夹下照片的名字,日期,坐标，
def getExifData(dirpath):    
    latLons=[]
    for root, dirs, files in os.walk(dirpath):
        print('根目录:{0},文件夹:{1},文件数:{2}'.format(root,dirs,len(files)))
        files.sort()
        for f in files:
            exif=extractExif('{0}/{1}'.format(dirpath,f))
            if exif:                
                latLons.append(exif)
            else:
                print(f,'exif is None')

    #按照拍摄时间排序
    for i in range(0,len(latLons)):
        for j in range(i,len(latLons)):
            if latLons[i][1] > latLons[j][1]:
                tmp = latLons[j]
                latLons[j] = latLons[i]
                latLons[i] = tmp
    return latLons

if __name__ == "__main__":
    wpt='./photo' #图片文件路径
    latLons = getExifData(wpt)
    if latLons:
        print(latLons)
    else:
        print('latLons is None')