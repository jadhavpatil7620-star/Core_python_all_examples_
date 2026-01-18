# print("Hello World!")


# Addition of Two Numbers

# num1=int(input("Enter First Number: "))
# num2=int(input("Enter Second Number: "))
# print("The Addition of Two Numbers: ",num1+num2)


# All arithmetic operations between two numbers.


# print("Substraction of two numbers: ",num1-num2)
# print("Multiplication of two numbers: ",num1*num2)
# print("Division two numbers: ",num1/num2)
# print("Modules of two numbers: ",num1%num2)
# print("Floor of two numbers: ",num1//num2)

# Check number is even or odd

# a=int(input("Enter a number: "))
# if a%2==0:
#     print("Given number is even.")
# else:
#     print("Given number is odd.")
    
    
# Number is divisible by 7 or not
# a=int(input("Enter a number: "))
# if a%7==0:
#     print("Given number is divisible by 7.")
# else:
#     print("Given number is not divisible by 7.")

# num=int(input("Enter a number: "))
# a=1
# if num%a==0:
#     print(f"Given number is divisible by {num}.")
# else:
#     print(f"Given number is not divisible by {num}.")

# Area of rectangle
# l=int(input("Enter a length of rectangle: "))
# b=int(input("Enter breadth of rectangle: "))
# print("Area of rectangle is: ",l*b)

# Wap to find the perimeter of rectangle
# print("Perimeter of rectangle is: ",2*(l+b))

# Area of circle
# r=int(input("Enter radius of circle: "))
# pi=3.14
# print("Area of circle is: ",pi*r*r)
# Perimeter=2*pi*r
# print("Perimeter of circle is:",2*pi*r)

# Find BMI
# weight=float(input("Enter weight in kg: "))
# height=float(input("Enter height in meters: "))
# bmi=weight/(height**2)
# print("BMI is: ",bmi)

# Wap to calculate percentage of 5 subject
# sci=float(input("Enter marks of science: "))
# math=float(input("Enter marks of math: "))
# eng=float(input("Enter marks of english: "))
# his=float(input("Enter marks of history: "))
# phy=float(input("Enter marks of physics: "))
# total=sci+math+eng+his+phy
# print("Total marks of 5 subject is: ",total)
# avg=total/5
# print("Average of 5 subjects is: ",avg)
# percentage=(total/500)*100
# print("Percentage of 5 subject is: ",percentage)




# num=int(input("Enter a number: "))
# if num%2==0:
#     print("The given number is even.")
# else:
#     print("The given number is odd.")

# positive=1
# negative=-1
# num=int(input("Enter a number :"))
# if num==positive:
#     print(num,"is positive number.")
# elif num==negative:
#     print(num,"is negative number.")
# else:
#     print(num,"is zero.")


# num1=int(input("Enter first number :"))
# num2=int(input("Enter second number :"))
# num3=int(input("Enter third number :"))
# if num1>num2 and num1>num3:
#     print(num1,"is the largest number.")
# elif num2>num1 and num2>num3:
#     print(num2,"is the largest number.")
# else:
#     print(num3,"is the largest number.")


# largest=max(num1,num2,num3)
# print(largest,"is the largest number.")


m=5
for i in range(m-1,0,-1):
    print(" "*(m-i)+"*"*(2*i-1))