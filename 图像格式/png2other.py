from wand.image import Image
with Image(filename = '../img/kanaer.png') as img:
    # img.resize(300,300) # width, height
    img.save(filename = '../img/kanaer.jpg') # png, jpg, bmp, gif, tiff All OK