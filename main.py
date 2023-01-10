from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os


for filename in os.listdir('images'):
    my_image = Image.open('images\\' + filename)
    I1 = ImageDraw.Draw(my_image)
    myFont = ImageFont.truetype('arial.ttf', 30)
    I1.text((10, 10), filename, font = myFont, fill = 'white', stroke_width = 2, stroke_fill='black')
    my_image.save('images\\legendado_' + filename)
    my_image.close()


