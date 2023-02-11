print('WORKING WITH IMAGES')

#import the pillow library
from PIL import Image
import os

#change cwd
os.chdir('/home/ag/Documents/python/pythonLearning/Working with images/')

mac = Image.open('example.jpg')

#type 
print(type(mac))   #o/p -> <class 'PIL.JpegImagePlugin.JpegImageFile'>

#show image
#mac.show()

#file information
print(f'file name -> {mac.filename}, size -> {mac.size}, file disc -> {mac.format_description}')

#crop the image
pencils = Image.open('pencils.jpg')

#crop all corners
TopLeft = pencils.crop((0,0,1950/4,1300/4))
BottomLeft = pencils.crop((0,1200,1950/4,1300))
TopRight = pencils.crop((1750,0,1950,1300/4))
BottomRight = pencils.crop((1750,1100,1950,1300))

#pencils.show()
#TopLeft.show()
#TopRight.show()
#BottomLeft.show()
#BottomRight.show()

#crop the mac from mac image
x = 1993/2 - 120
y = 1257/2 + 220
w = x + 265
h = 1257

computor = mac.crop((x,y,w,h))

#pasting cropped part to actual image
#this affects only the mac object and not the actual image
mac.paste(im=computor,box=(0,0))
#mac.show()

#resize
#mac.resize((2000,1500)).show()

#rotate
#mac.rotate(90).show()


#color Transperancy
#RGBA - > Red,Green,Blue,Alpha
#value of all R,G,B,A go from 0 to 255
#if alpha = 0 -> image is Transperant
#if alpha = 255 ->  image is Opeque
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png').convert('RGB')     #putalpha funnction was giving error on png images, so use convert('RGB') https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil/52307690#52307690


#making purple
#put appropriate alpha value 
red.putalpha(120)
blue.putalpha(100)

blue.paste(im=red,box=(0,0),mask=red)

blue.save('purple.png')


