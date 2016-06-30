# import turtle as t
from collections import Iterable
import random
import math
from PIL import Image, ImageDraw
import time
import pyautogui

im = Image.new('RGBA', (10, 10), 'white')
color = "black"
draw = 0
dim = 0

# t.speed(10)
colors = ["red", "blue", "green", "pink", "violet", "yellow"]


def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable):
            for x in flatten(item):
                yield x
        else:
            yield item


def randomSign():
    if random.random() < 0.499999:
        return 1
    else:
        return -1


def unFlatten(lst):
    # print(lst)
    if len(lst) == 2:
        return lst
    else:
        L = len(lst)
        lst1, lst2 = lst[:int(L / 2)], lst[int(L / 2):]
        return [unFlatten(lst1), unFlatten(lst2)]


def createPoints(n):
    print("Dimention: ", n)
    start_a = time.time()
    L = [0, 0]
    dist = 1300
    0
    x = 0;
    while x < n:
        print(x)
        if (x < 3):
            pass
        else:
            dist = int(float(dist) * 1.3)
        # print("begin loop: ",L)
        deltaX = randomSign() * int(dist * random.random())
        deltaY = randomSign() * int(math.sqrt((dist ** 2) - (deltaX ** 2)))
        # print("delta X: ",deltaX, " delta Y: ",deltaY)
        flatL = list(flatten(L))
        # print("flat list: ",flatL)
        newL = []
        for i in range(len(flatL)):
            if i % 2 == 0:
                newL.append(flatL[i] + deltaX)
            else:
                newL.append(flatL[i] + deltaY)
        LCopy = newL
        # print("newL: ",newL)
        # print("unflattened: ",unFlatten(LCopy))
        L = [L, unFlatten(LCopy)]
        x += 1
        # print("end loop: ",L)
    print("\nList of points created.")
    end_a = time.time()
    time_a = end_a - start_a
    print("\nTime to create points: ", time_a, "\n")
    # print(L)
    return L


def line(x1, y1, x2, y2):
    t.up()
    t.setx(x1)
    t.sety(y1)
    t.down()
    t.goto(x2, y2)
    # print ("Line drawn from (",x1,", ",y1,") to (",x2,", ",y2,").")


def Draw(lst, n):
    global color
    global draw
    global dim
    # print(lst)
    # print(lst[0][0])
    # print(str(lst[0][0]).isdigit())
    if (str(lst[0][0])).isdigit() or (str((-1) * lst[0][0]).isdigit()):
        # line(lst[0][0],lst[0][1],lst[1][0],lst[1][1])
        draw.line(((lst[0][0] + dim[0] + 150, lst[0][1] + dim[2] + 150),
                   (lst[1][0] + dim[0] + 150, lst[1][1] + dim[2] + 150)), fill=color, width=1)
    else:
        print(n)
        Draw(lst[0], n - 1)
        Draw(lst[1], n - 1)
        # t.pencolor(colors[n%6])
        color = colors[n % 6]
        lst1, lst2 = list(flatten(lst[0])), list(flatten(lst[1]))
        for i in range(0, len(lst1), 2):
            # line(lst1[i],lst1[i+1],lst2[i],lst2[i+1])
            draw.line(((lst1[i] + dim[0] + 150, lst1[i + 1] + dim[2] + 150),
                       (lst2[i] + dim[0] + 150, lst2[i + 1] + dim[2] + 150)), fill=color, width=1)


def Max(lst):
    flatL = list(flatten(lst))
    Xmin = abs(flatL[0])
    Xmax = abs(flatL[0])
    Ymin = abs(flatL[0])
    Ymax = abs(flatL[0])
    for i in range(0, len(flatL), 2):
        if flatL[i] > Xmax:
            Xmax = flatL[i]
        if flatL[i] < Xmin:
            Xmin = flatL[i]

    for i in range(1, len(flatL), 2):
        if flatL[i] > Ymax:
            Ymax = flatL[i]
        if flatL[i] < Ymin:
            Ymin = flatL[i]
    L = [abs(Xmin), Xmax, abs(Ymin), Ymax]
    # print("\n",L)
    return (L)


def drawArg(n):
    global draw
    global dim

    points = createPoints(n)

    start_b = time.time()
    dim = Max(points)
    im = Image.new('RGBA', (dim[0] + dim[1] + 300, dim[2] + dim[3] + 300), 'white')
    draw = ImageDraw.Draw(im)
    Draw(points, n)
    im.save('drawing_' + str(n) + '_2.png')
    end_b = time.time()
    time_b = end_b - start_b
    print("complete.\nTime to create image: ", time_b)

    # print(list((flatten([[ [0,1], [2,3,4] ], [2,5]]))))
    # print(unFlatten([1,2,3,4,5,6,7,8]))
    '''
for i in range(21):
    createPoints(i)
    print("\n################################################\n")
    '''


drawArg(16)




