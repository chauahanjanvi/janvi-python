Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=6
>>> b=3
>>> print(a+b)
9
>>> print(a-b)
3
>>> print(a/b)
2.0
>>> x=12
>>> print(x) #assigns value 12 to x
12
>>> #unary Minus
>>> a=4
>>> print(-a)
-4
>>> 
>>> #Relational Operators
>>> p=6
>>> q=4
>>> print(p>q)  #true
True
>>> print(p==q) #false
False
>>> 
>>> #logical operators
>>> x=true
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x=true
NameError: name 'true' is not defined
>>> x=True
>>> y=False
>>> print(x and y)   #false
False
>>> print(x or y)    #true
True
>>> print(not x)
False
>>> 
>>> #boolean values
>>> is_pass  = true
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    is_pass  = true
NameError: name 'true' is not defined
>>> 
>>> is_pass = True
>>> print(is_pass)  #true
True
>>> 
>>> #bitwise operators
>>> a=5
>>> b=3
>>> print(a&b)  #1
1
>>> print(a/b)   #7
1.6666666666666667
>>> 
>>> #membership operators
>>> #bitwise operators
>>> x=0
>>> y=0
>>> print(x^y)
0
>>> x=3
>>> y=4
>>> print(x^y)
7
>>> print(x&y)
0
>>> print(x/y)
0.75
>>> 
>>> 
>>> #membership operators
>>> numbers=[1,2,3,4]
>>> print(2 in numbers)
True
>>> print(5 not in numbers)
True
>>> 
>>> 
>>> #identify operators
>>> x=10
>>> y=10
>>> print(x is y)
True
>>> print(x is not y)
False
>>> 