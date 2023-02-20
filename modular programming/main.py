import operators
# x = operators.add(12,34)
# print(x)

# y = operators.subtract(34,12)
# print(y)

# from operators import add
# z = add(21,14)
# print(z)

# w = operators.divide(6,3)
# print(w)
import trigonometry
import others
# a = others.cube(9)
# print(a)

operator=input("Enter operator:")

if operator == "cube":
  num = eval(input("Enter your number:"))
  q = others.cube(num)
  print(q)

elif operator == "sin":
    angle = eval(input("enter angle in degrees: "))
    sin_of_angle = trigonometry.get_sine(angle)
    print(sin_of_angle)

elif operator =="cos":
     angle = eval(input("Enter angle in degrees:"))
     cos_of_angle = trigonometry.get_cos(angle)
     print(cos_of_angle)

elif operator =="tan":
     angle = eval(input("Enter angle in degrees:"))
     tan_of_angle = trigonometry.get_tan(angle)
     print(tan_of_angle)

else:
 num1=eval(input("Enter your number 1:"))
 num2=eval(input("Enteryour number 2:"))

if operator == "+":
    x=operators.add(num1,num2)
    print(x)

elif operator == "-":
    y=operators.subtract(num1,num2)
    print(y)


elif operator == "/":
    w=operators.divide(num1,num2)
    print(w)

elif operator == "*" or  operator=="x" or operator== "X":
    z=operators.multiply(num1,num2)
    print(z)



