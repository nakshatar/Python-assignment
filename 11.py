import math
PI = 3.14
print("to find the area of circle")
radius = float(input(' Please Enter the radius of a circle: '))
area = PI * radius * radius
circumference = 2 * PI * radius
 
print(" Area Of a Circle = %.2f" %area)
print(" Circumference Of a Circle = %.2f" %circumference)
print("to find the the area of triangle")
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ",round(area,2))
print("to find the area of square")
A=int(input("enter the length of one side of the square"))
Ar=(A*A)
print("area of the square is:",Ar)