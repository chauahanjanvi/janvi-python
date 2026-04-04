"""print("program start")
try:
    result=10/0
    print("Result:",result)"""

"""except:
    print("An error occured.Division By zero is not allowed")
    print("Program End")"""

"""try:
    number=int(input("Enter a Number:"))
    print("you entered:",number)

except ValueError:
    print("Error:Please Enter a valid integer value:")        
"""

"""try:
    a=int(input("Enter a Number:"))
    b=int(input("Enter another Number:"))
    result=a/b
    print("Result:",result)
except ZeroDivisonError:
    print("Error:CAnnot divid By zero..")
except ValueError:
    print("Error,please Enter Only integer..")    
"""

"""try:
    a=-10
    b=-0
    result=a/b
    print(result)
except ZeroDivisionError:
    print("Error :divison by zero.") 
finally:
    print("this line always runs(finally block).")       
"""

try: 
    user_number = int(input("Enter a number:"))
    result = 100/user_number
except ValueError:
    print("Error:Invalid number format")
except ZeroDivisionError:
    print("Error:Cannot Divide By zero")
else:
    print("sucess.!!Result:",result)            
