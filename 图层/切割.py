# coding:utf-8
import os

from PIL import Image


def cropimg(file):
    folder,f = os.path.split(file)
    fname, prefix = os.path.splitext(f)
    pil_IMG = Image.open(file)
    letter1 = pil_IMG.crop((0, 0, 18, 27))
    letter2 = pil_IMG.crop((18, 0, 28,27))
    letter3 = pil_IMG.crop((28, 0, 40, 27))
    letter4 = pil_IMG.crop((40, 0, 72, 27))
    letter1.save(folder+'/letter/'+fname+'_1'+prefix)
    letter2.save(folder+'/letter/'+fname+'_2'+prefix)
    letter3.save(folder+'/letter/'+fname+'_3'+prefix)
    letter4.save(folder+'/letter/'+fname+'_4'+prefix)

path='/MacData/GOPATH/src/captcha-ocr/download/72*27'
for file in os.listdir(path):
    f=path+'/'+file
    if os.path.isfile(f):
        cropimg(f)

