from getExifData import getExifData

def writeGeojson(file,latLons):
    #按照拍摄时间排序    
    for i in range(0,len(latLons)):
        for j in range(i,len(latLons)):
            if latLons[i][1] > latLons[j][1]:
                tmp = latLons[j]
                latLons[j] = latLons[i]
                latLons[i] = tmp
    index = 1
    for photo in latLons:
        print(photo)
        file.writelines('{"type": "Feature","properties": {"cartodb_id":"' + str(index) + '"')        
        file.writelines(',"photo date":"' + str(photo[1]) + '","image":"' + 'https://github.com/mutou8bit/PhotoMap/tree/master/photo/' + photo[0] + '"')
        if index == len(latLons):
            file.writelines('},"geometry": {"type": "Point","coordinates": [' + str(photo[2]) + ',' + str(photo[3]) + ']}}\n')
        else:
            file.writelines('},"geometry": {"type": "Point","coordinates": [' + str(photo[2]) + ',' + str(photo[3]) + ']}},\n')
        index += 1

if __name__ == "__main__":
    wpt='./photo' #图片文件路径
    geojsonFile = open("photo.geojson", "w")
    geojsonFile.writelines('{\n"type": "FeatureCollection","features": [\n')    
    latLons = getExifData(wpt)
    writeGeojson(geojsonFile, latLons)
    geojsonFile.writelines(']}\n')

    geojsonFile.close()
