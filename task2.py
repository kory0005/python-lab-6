from gfxhat import lcd
from PIL import Image, ImageDraw

coordinateX = int(input('Please enter the x coordinate between 0px and 127px: '))
coordinateY = int(input('Please enter the y coordinate between 0px and 63px: '))

def displayObject(obj,x,y):
    for line in range(len(obj)):
        for num in range(len(obj[line])):
            if obj[line][num] == 1:
                lcd.set_pixel((x + (num*2)), (y + (line*2)), 1)
                lcd.set_pixel((x + num*2 + 1), (y + line*2 + 1), 1)
                lcd.set_pixel((x + num*2) , (y + line*2 + 1), 1)
                lcd.set_pixel((x + num*2 + 1), (y + line*2), 1)
    lcd.show()

if coordinateX > 127:
    coordinateX = 0
elif coordinateY > 63:
    coordinateY = 0
lcd.show()


f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

displayObject(f1, coordinateX, coordinateY)



pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

displayObject(pm, (coordinateX + 30), (coordinateY))