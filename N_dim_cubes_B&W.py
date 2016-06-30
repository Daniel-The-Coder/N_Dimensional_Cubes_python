import turtle as t
from collections import Iterable
import random
import math

cur = 0




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
    L = [0, 0]
    dist = 100
    x = 0;
    while x < n:
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
    return L


def line(x1, y1, x2, y2):
    t.up()
    t.setx(x1)
    t.sety(y1)
    t.down()
    t.goto(x2, y2)
    # print ("Line drawn from (",x1,", ",y1,") to (",x2,", ",y2,").")


def draw(lst, n):
    # print(lst)
    # print(lst[0][0])
    # print(str(lst[0][0]).isdigit())
    if (str(lst[0][0])).isdigit() or (str((-1) * lst[0][0]).isdigit()):
        line(lst[0][0], lst[0][1], lst[1][0], lst[1][1])
    else:
        draw(lst[0], n - 1)
        draw(lst[1], n - 1)
        lst1, lst2 = list(flatten(lst[0])), list(flatten(lst[1]))
        for i in range(0, len(lst1), 2):
            line(lst1[i], lst1[i + 1], lst2[i], lst2[i + 1])


def drawArg(n):
    draw(createPoints(n), n)


# print(list((flatten([[ [0,1], [2,3,4] ], [2,5]]))))
# print(unFlatten([1,2,3,4,5,6,7,8]))
# createPoints(3)
drawArg(3)

