import calendar
print(calendar.month(2025,9))


"""
February 2025
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28

"""

import math
def carea(r):
    return math.pi*r*r
r=float(input("enter the radious"))
area=carea(r)
print(area)

print("-----------------------------------")
import random
print(random.randint(0,5))
print(random.random())
print(random.random()*100)
l=[1,4,True,800,"python",27,"hello"]
print(random.choice(l))

print("-----------------------------------")

import datetime
from datetime import date
import time
print(time.time)
print(date.fromtimestamp(454554))


