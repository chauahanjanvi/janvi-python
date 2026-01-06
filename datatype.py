Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hello world");
hello world
int x="20"
SyntaxError: invalid syntax
x=20
print(x)
20
x=20.5
print(x)
20.5
x=apple,banana,cherry
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x=apple,banana,cherry
NameError: name 'apple' is not defined. Did you mean: 'tuple'?
x=1j
print(x)
1j
x=["apple","banana","cherry"]
print(x)
['apple', 'banana', 'cherry']
x=["janvi","nirali","anandi"]
print(x)
['janvi', 'nirali', 'anandi']
x=true
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x=true
NameError: name 'true' is not defined. Did you mean: 'True'?
x="true"
print(x)
true
