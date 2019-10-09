from getExifData import getExifData

def writeGeojson(latLons):
    #按照拍摄时间排序
    

if __name__ == "__main__":
    wpt='./photo' #图片文件路径
    geojsonFile = open("photo.geojson", "w")
    geojsonFile.writelines('{\n"type": "FeatureCollection","features": [\n')    
    latLons = getExifData(wpt)
    writeGeojson(latLons)
    geojsonFile.writelines(']}\n')

    geojsonFile.close()
