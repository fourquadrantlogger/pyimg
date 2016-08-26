from PIL import Image

pil_IMG=Image.open('img/example.jpg')
gray=pil_IMG.convert('L')
gray.save("img/gray.jpg")

thumb=pil_IMG.copy()

print id(thumb),id(pil_IMG)
thumb.thumbnail((100,100))
thumb.save("img/thumb.jpg")

region=pil_IMG.crop((0,0,100,100))
region=region.rotate(180)

pasteimg=pil_IMG.copy()
pasteimg.paste(region,(0,0,100,100))
pasteimg.save('img/region.jpg')

