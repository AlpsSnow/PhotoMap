#!/usr/bin/env python

import os
from PIL import Image

size = 512, 512

def resize(photo_path):
    for root, dirs, files in os.walk(photo_path):
        print('根目录:{0},文件夹:{1},文件数:{2}'.format(root,dirs,len(files)))
        for f in files:
            outfile = f.replace(".jpg", ".thumbnail.jpg")
            try:
                im = Image.open('{0}/{1}'.format(photo_path,f))
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('./resize/{0}'.format(outfile), "JPEG")
            except IOError:
                print('cannot create thumbnail for{0}'.format(outfile))


if __name__ == "__main__":
    resize('./photo')