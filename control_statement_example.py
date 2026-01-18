# # 1.WAP to check the given number is greater than 0 or not.
# num = int(input("Enter a number:"))
# if num > 0:
#     print(f"{num} is grater than 0.")
# else:
#     print(f"{num} is less than 0.")
    
    
# # 2.Write a program to print:
# #     ==>"Excellent" if marks ≥ 80
# #     ==>"Good" if marks ≥ 50 and < 80
# #     ==>"Fail" if marks < 50
# marks = float(input("Enter your marks which is get you in exam:"))
# if marks >= 80:
#     print(f"You are Excellent in study.")
# elif marks >= 50 and marks <80:
#     print(f"You are Good in study.")
# else:
#     print(f"You are fail in exam.")
    

# # 3.Write a program to check:
# #     ==>"Child" if age < 13
# #     ==>"Teenager" if age between 13 and 19
# #     ==>"Adult" if age ≥ 20
# age = int(input("Enter your age:"))
# if age < 13:
#     print(f"{age} you are at the child stage.")
# elif age >= 13 and age <= 19:
#     print(f"{age} you are in Teenager stage.")
# elif age >= 20:
#     print(f"{age} you are in Adult stage.")
# else:
#     print(f"{age} Invalid age or please Enter correct age.")
    

# # 4.Write a program to check:
# #     ==>if a number is positive
# #     ==>and if it is divisible by 5
# num = int(input("Enter a number:"))
# if num > 0:
#     if num % 5 == 0:
#         print(f"{num} is positive as well as it is divisible by 5.")
#     else:
#         print(f"{num} is not divisible by 5.")
# else:
#     print(f"{num} is not a positive number.")
    

# # 5.Write a program to check whether a character is a vowel or consonant.
# ch = input("Enter a character would you like to write:").lower()
# if ch in ('a','e','i','o','u'):
#     print(f"{ch} is the vowel character.")
# else:
#     print(f"{ch} is the constant character.")
    
# # 6.Write a program to check whether a year is a leap year or not.
# year = int(input("Enter a year(like that 2003):"))
# if year % 4 == 0:
#     print(f"{year} is the leap year.")
# else:
#     print(f"{year} is not a leap year.")
    
# # 7.Write a program to check whether a number is divisible by both 3 and 5.
# num = int(input("Enter a number:"))
# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by both 3 and 5.")
# else:
#     print(f"{num} is not divisible by 3 and 5.")
    
# 8.Write a program to find the largest of three numbers.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
if num1>num2 and num1>num3:
    print(f"{num1} is greater than {num2} and {num3}")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater than {num1} and {num3}")
elif num3>num1 and num3>num2:
    print(f"{num3} is greater than {num1} and {num2}.")
else:
    print("Please enter a valid numbers and try again.")
    
# # 9.Write a program to check whether a character is:
# #     ==>Uppercase
# #     ==>Lowercase
# #     ==>Digit
# #     ==>Special character
# chr = input("Enter a characturer:")
# if len(chr) != 1:
#     print("Please enter only one character.")
# elif chr.isupper():
#     print(f"{chr} is an Uppercase character.")
# elif chr.islower():
#     print(f"{chr} is a Lowercase character.")
# elif chr.isdigit():
#     print(f"{chr} is a Digit character.")
# else:
#     print(f"{chr} is a Special character.")

# # 10.WAP to calculate elictrcity bill based on below criteria:
# # for first 100 uints RS. 0 per unit
# # for next 100 uints RS. 5 per unit
# # for <=200 units RS. 10 per unit
# units = int(input("Enter the total units consumed in a month:"))
# if units<=100:
#     bill_amount = units + 0
# elif units<=200:
#     bill_amount = (units - 100) * 5
# else:
#     bill_amount = (100 * 5) + (units - 200) * 10
# print(f"Your total electricity bill for {units} units is: RS.{bill_amount}")

