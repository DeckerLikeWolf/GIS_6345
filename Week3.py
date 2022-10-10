from tkinter.tix import DisplayStyle


print('GIS_6345')
minutes = 105
minutes / 60 
hours = minutes // 60
hours
remainder = minutes % 60
remainder
6 == 6
6 == 7
6 != 7
7 > 6
6 < 7
6 == 7 or 6 < 7 
x = 6
if x > 5:
    print('x is positive')
    x = 4
    if x % 2 == 0:
        print('x is even')
    else:
        print('x is odd')
import math
import time
time.time()
#epoch time
epoch = int(time.time())
#days since epoch
def todays_time(since_epoch):
#current time tince epoch
    hr_since = since_epoch // 60 // 60
    current_hr = hr_since - (hr_since // 24) * 24
    min_since = since_epoch // 60
    current_min = min_since - (min_since // 60) * 60
    sec_since = math.floor(epoch)
    current_sec = sec_since - (sec_since // 60) * 60
    return current_hr, current_min, current_sec

def number_days_since_epoch(epoch):
#days since epoch
    days = epoch // 60 // 60 // 24
    return days 
print(todays_time(epoch))
print(number_days_since_epoch(epoch))

import math
a= 2
b= 2
c= 2
n= 7
def check_fermat()

def check_fermat(a, b, c, n):
    if n >2 and (a**n + b**n == c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that does not work')

def input_values():
    a = int (input('enter value for a: '))
    b = int (input('enter value for b: '))
    c = int (input('enter value for c: '))
    n = int (input('enter value for n greater than 2: '))
    return(check_fermat(a, b, c, n))
'''compare function that takes two values,
 x & y, returns 1 if x > y, 0 if x==y, 
 & -1 if x<y'''
def func(x,y):
    if x > y:
        return 1
    elif x ==y:
        return 0
    else:
        return -1

func(2,7)







