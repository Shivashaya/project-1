import math 
print(""" 
press -  
1 - Addition(x, y) 
2 - subtraction(x,y) 
3-multiplication(x,y) 
4 - division(x, y) 
5- modulus(x, y) 
6 - exponent(x, y) 
7 - tan(x, y) 
8 - sin(x)    
9 - cos(x)  
10 - radian to degree(x)
11 - square root
""") 
o = input("") 
if o == "1": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
    print(x + y) 
elif o == "2": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -"))  
    print(x-y) 
elif o == "3": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
elif o == "4": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
    print(x/y) 
elif o == "5": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
    print(x%y)
elif o == "6": 
    x = int(input(" number -")) 
    y = int(input("Power -")) 
    print(x**y) 
elif o == "7": 
    x = int(input("1st number -")) 
    y = int(input("2nd number -")) 
    print(math.tan(x)) 
elif o == "8": 
    x = int(input(" Number -")) 
     
    print(math.sin(x)) 
elif o == "9": 
    x = int(input("Number -")) 
    cos(x) 
elif o == "10": 
    x = int(input("Number -")) 
    print(x*(180/3.14))
elif o == "11":
    x = int(input("Number -"))
    print(math.sqrt(x))




          
