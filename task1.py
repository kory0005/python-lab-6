from gfxhat import lcd, touch
from PIL import Image, ImageFont, ImageDraw
import signal
import sys, os


# setup a pixel
status = True
x = int(127/2)
y = int(63/2)
lcd.set_pixel(x, y, 1)
lcd.show()


# Text
def displayText(text,lcd,x,y):
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    # print("display TEXT in terminal")
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

displayText('Etch a Sketch', lcd, 25, 5)


#  buttons
def handler(channel, event):
    global y, x, status
    print("Got {} on channel {}".format(event, channel))
    if (channel == 2 and event == 'press'): #  QUIT
        print("QUIT")
        lcd.clear()
        lcd.show()
        os._exit(1)
        return status
    elif (channel == 4 and event == 'press'): # RESET
        x = 60
        y = 30
        lcd.clear()
        lcd.set_pixel(x, y, 1)
        displayText('Etch a Sketch', lcd, 20, 10)
        # print("RESET")
    elif (channel == 1 and event == 'press'): # DOWN
        # print("DOWN")
        y = y + 1
        if y > 63:
            y = 0
        lcd.set_pixel(x, y, 1)
    elif (channel == 0 and event == 'press'): # UP
        # print("UP")
        y = y - 1   
        if y < 0:
            y = 63
        lcd.set_pixel(x, y, 1)
    elif (channel == 3 and event == 'press'): # LEFT
        # print('LEFT')
        x = x - 1
        if x < 0:
            x = 127  
        lcd.set_pixel(x, y, 1) 
    elif (channel == 5 and event == 'press'): # RIGHT
        # print('RIGHT')
        x = x + 1
        if x > 127:
            x = 0   
        lcd.set_pixel(x, y, 1) 

    lcd.show()
    return True
   

for z in range(6):
    print(status)
    touch.on(z, handler)
    print(status)
    if (status == False):
        print(status)
        break

signal.pause()
