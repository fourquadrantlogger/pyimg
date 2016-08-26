# coding:utf-8

from matplotlib.pyplot import imshow, show, title, figure, gray, contour, axis, hist
from numpy.ma import array
from PIL import Image

img=Image.open('captcha/example3.jpg')

imgarray=array(img.convert('L'))

# 新建一个图像
figure()
# 灰度
gray()
# 在原点的左上角,显示轮廓图像
contour(imgarray,origin='image')
axis('equal')
title('aijiang')

# 绘制直方图
figure()
hist(imgarray.flatten(),128)
show()

