import os
import math
import numpy as np
import cv2
import time
#from Elevation import color

lerp = lambda x, minV, maxV: (x - minV)/ (maxV - minV)

def myDemMap(height,min=0,max=8000):
    return lerp((abs(height)*1.0),min,max)
    #h = abs(height)
    #h = h if h>0 else 0
    #h = h if h<9000 else 9000
    #r=g=b=lerp(h,0,9000)
    #return (r,g,b)
    # 
    # if height < 0:
    #     return (0,0,lerp(height,-100,0))

def colorMap(img):
    #arr[arr > 255] = x
    img[img < 0] = 0
    img[img > 9000] = 9000
    res = img * 255.0 / 9000.0
    return cv2.resize(res, (0,0), fx=0.5, fy=0.5) 

def readHGT(filename):
    siz = os.path.getsize(filename)
    dim = int(math.sqrt(siz/2))

    assert dim*dim*2 == siz, 'Invalid file size'

    return np.fromfile(filename, np.dtype('>i2'), dim*dim).reshape((dim, dim))

def process(filename):
    data = readHGT(filename)
    img = colorMap(data)

    NAME =filename.split('/')[1]
    cv2.imwrite("PNG/"+NAME[:-3]+"png", img)

# millis = int(round(time.time() * 1000))
# process('HGT/S33W072.hgt')
# print "millis:",int(round(time.time() * 1000)) - millis
# cv2.waitKey(0)

millis = int(round(time.time() * 1000))
i=0.0
for line in open("the_world.txt",'r'):
    process("HGT/"+line[:-1])
    i+=1
delta = int(round(time.time() * 1000)) - millis
print "millis:",delta
print "promedio por imagen:",delta/i
print "total de imagenes:",i