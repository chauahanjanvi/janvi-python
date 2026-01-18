Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#print message
print("hello atmiya university..")
hello atmiya university..
#sum
a=input("enter value:")
enter value:7
b=input("enter value:")
enter value:3
result=int(a)+int(b)
print(result)
10
#odd,even
num=int(input("enter value:"))
enter value:66
if(num%2==0):
    print("this number is odd.")
else:
    print("this number is even.")

    
this number is odd.
#leap year
year=int(input("enter a year:"))
enter a year:2030
if(year%4==0 and year%100!=0):
    print("leap year.")
else:
    print("not a leap year.")

    
not a leap year.
#PI value
import math
print(math.pi)
3.141592653589793
#constant value
a=15
print(a)
15
#square of number
num=int(input("enter number:"))
enter number:6
square=num*num
print("square=",square)
square= 36
#area of circle
import math
r=float(input("enter radius:"))
enter radius:55
print(math.pi * r * r)
9503.317777109125
#check data type
a=input("enter anything:")
enter anything:99
print(type(a))
<class 'str'>
#use math function
import math
>>> print("square root:",math.sqrt(16))
square root: 4.0
>>> print("power:",math.pow(2,5))
power: 32.0
>>> print("PI value:",math.pi)
PI value: 3.141592653589793
>>> #find power
>>> a=int(input("enter base number:"))
enter base number:11
>>> b=int(input("enter power:"))
enter power:4
>>> print("answer=", a**b)
answer= 14641
>>> #positive,negative
>>> n=int(input("enter number:"))
enter number:38
>>> if n > 0:
...     print("positive number.")
... elif n < 0:
...     print("negative number.")
... else:
...     print("zero.")
... 
...     
positive number.
