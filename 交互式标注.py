# coding:utf-8
from PIL import Image
from matplotlib.pyplot import imshow, ginput, show
from numpy import array

im=array(Image.open('img/example.jpg'))
imshow(im)

print "单击 3次"
x=ginput(3)
print '你单击了',x
show()