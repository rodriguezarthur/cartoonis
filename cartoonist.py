import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyautogui
from pynput import mouse

white = [255, 255, 255]
black = [0, 0, 0]
ligthgrey = (193, 193, 193)
darkgrey = (80, 80, 80)
red = (239, 19, 11)
darkred = (116, 11, 7)
orange = (255, 113, 0)
darkorange = (194, 56, 0)
yellow = (255, 228, 0)
darkyellow = (232, 162, 0)
green = (0, 204, 0)
darkgreen = (0, 70, 25)
lightgreen = (0, 255, 145)
darkgreen2 = (0, 120, 93)
lightblue1 = (0, 178, 255)
lightblue2 = (0, 86, 158)
blue = (35, 31, 211)
darkblue = (14, 8, 101)
purple = (163, 0, 186)
darkpurple = (85, 0, 105)
pink = (223, 105, 167)
darkpink = (135, 53, 84)
beige = (255, 172, 142)
darkbeige = (204, 119, 77)
brown = (160, 82, 45)
darkbrown = (99, 48, 13)

colors2= [black, ligthgrey, darkgrey, red, darkred, orange, darkorange, yellow, darkyellow, green, lightgreen, darkgreen, darkgreen2, lightblue1, lightblue2, blue, darkblue, purple, darkpurple, pink, darkpink, beige, darkbeige, brown, darkbrown]

"""
darkgrey = [127, 127, 127]
lightgrey = [195, 195, 195]
darkred = [136, 0, 21]
brown = [185, 122, 87]
red = [237, 28, 36]
pink = [255, 174, 201]
orange = [255, 127, 39]
darkyellow = [255, 201, 14]
yellow = [255, 242, 0]
lightyellow = [239, 228, 176]
green = [34, 177, 76]
lightblue1 = [0, 162, 232]
lightblue2 = [153, 217, 234]
blue = [63, 72, 204]
bluefade = [112, 146, 190]
purple = [163, 73, 164]
lightpurple = [200, 191, 231]

colors = [white, black, lightgrey, darkgrey, darkred, brown, red, pink, orange, darkyellow, yellow, lightyellow, green, lightblue1, lightblue2, blue, bluefade, purple, lightpurple]
"""


def computeDifference(color1, color2):
    return abs(color1[0] - color2[0]) + abs(color1[1] - color2[1]) + abs(color1[2] - color2[2])

def findNearestColor(color):
    nearestColor = white
    smallestDiff = computeDifference(color, white)
    for clr in colors2:
        newDiff = computeDifference(color, clr)
        if newDiff < smallestDiff:
            smallestDiff = newDiff
            nearestColor = clr
    return nearestColor

def fromImageToDraw(image):
    im = mpimg.imread(image)
    y = len(im)
    x = len(im[0])
    l = [[[0,0,0] for i in range(x)] for j in range(y)]
    pourcentage = 0
    nbpixel = 0
    n = x*y
    
    for i in range(y-1):
        for j in range(x-1):
            newColor = findNearestColor(im[i][j])
            l[i][j] = newColor
            
            nbpixel += 1
            if int(nbpixel/n * 100) > pourcentage:
                pourcentage = int(nbpixel/n * 100)
                print(str(pourcentage) + "%")
    
    plt.imshow(l)
    plt.show()
    
fromImageToDraw("Stitch.jpg")    

"""
mouse_x = 0
mouse_y = 0
drawing = False
def on_click(x, y, button, pressed):
    global drawing
    if pressed and not(drawing):
        drawing = True
        mouse_x, mouse_y = pyautogui.position()
        print("Converting the image...")
        l = fromImageToDraw("Stitch.jpg")
        print("Starting the draw !")
        for i in range(len(l)):
            for j in range(len(l[0])):
                if (l[i][j] == black):
                    pyautogui.click(x=1105, y=121, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == darkgrey):
                    pyautogui.click(x=1137, y=116, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == lightgrey):
                    pyautogui.click(x=1135, y=149, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == darkred):
                    pyautogui.click(x=1165, y=118, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == brown):
                    pyautogui.click(x=1169, y=150, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == red):
                    pyautogui.click(x=1195, y=115, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == pink):
                    pyautogui.click(x=1194, y=147, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == orange):
                    pyautogui.click(x=1223, y=116, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == darkyellow):
                    pyautogui.click(x=1227, y=147, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == yellow):
                    pyautogui.click(x=1260, y=117, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == lightyellow):
                    pyautogui.click(x=1258, y=151, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == green):
                    pyautogui.click(x=1288, y=119, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == lightgreen):
                    pyautogui.click(x=1286, y=148, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == lightblue1):
                    pyautogui.click(x=1316, y=119, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == lightblue2):
                    pyautogui.click(x=1316, y=149, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == blue):
                    pyautogui.click(x=1346, y=119, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == bluefade):
                    pyautogui.click(x=1346, y=149, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == purple):
                    pyautogui.click(x=1375, y=121, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                elif (l[i][j] == lightpurple):
                    pyautogui.click(x=1177, y=149, button="left")
                    pyautogui.click(x=mouse_x+j, y=mouse_y+i, button="left")
                else:
                    print("rien")
                    
listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    pass
    """