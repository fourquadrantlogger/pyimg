# coding:utf-8

from matplotlib.pyplot import imshow, show, title
from numpy.ma import array
from PIL import Image

img=Image.open('img/example.jpg')

imgarray=array(img)
imshow(imgarray)
title('aijiang')
show()

