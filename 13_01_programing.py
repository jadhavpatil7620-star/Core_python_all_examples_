# Check if a number is divisible by both 3 and 5
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by both 3 and 5.")
    
# else:
#     print(f"{num} is not divisible by both 3 and 5.")
    
    
# age = float(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")



# age = float(input("Enter your age: "))
# if age >= 18 and age <= 65:
#     print("You are eligible to work.")
# else:
#     print("You are not eligible to work.")



# age = float(input("Enter your age: "))
# if age >= 18 and age <= 18:
#     print("You are eligible for a driving license.")
# else:
#     print("You are not eligible for a driving license.") 
    

# age = float(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible for a credit card.")
# elif age >= 16:
#     print("You are eligible for a debit card.")
# else:
#     print("You are not eligible for a credit or debit card.") 
    
    
# student_marks = float(input("Enter your marks: "))
# if student_marks >= 95:
#     print("You have got an A+ grade.")
# elif student_marks >= 85:
#     print("You have got an A grade.")
# elif student_marks >= 75:
#     print("You have got a B grade.")
# elif student_marks >= 65:
#     print("You have got a C grade.")
# elif student_marks >= 50:
#     print("You have got a D grade.")
# elif student_marks >= 35:
#     print("You have been passed.")
# elif student_marks < 35:
#     print("You have been failed.")
# else:
#     print("You have not attempted the exam.")
    
    
    
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}.")
# else:
#     print(f"{num2} is greater than {num1}.")
    

    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /,%): ")
for i in operation:
    if operation == "exit":
        print("Exiting the program safely ! See you again.")
        break
    if operation == "+":
        print(f"The sum is: {num1 + num2}")
    elif operation == "-":
        print(f"The difference is: {num1 - num2}")
    elif operation == "*":
        print(f"The product is: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"The quotient is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    elif operation == "%":
        print(f"The modulus is: {num1 % num2}")
    else:
        print("Please enter a valid operation is given in list(+,-,*,/,%).")
    for i in operation:
        if operation == "exit":
            print("Exiting the program safely ! See you again.")
            break
        else:
            continue
print("Thank you for using the calculator.")
    
    
# num1 = int(input("Enter first number: "))
# print(f"The cube of {num1} is: {num1 ** 3}") 
