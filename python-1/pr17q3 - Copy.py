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



"""
4
0.41965502234629193
33.00312500015041
hello
-----------------------------------
<built-in function time>
1970-01-06
"""
