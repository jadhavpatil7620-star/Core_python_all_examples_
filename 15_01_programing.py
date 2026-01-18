# 1.For Loop Examples

# for i in range(1,51):
#     # print(i)
#     if i == 3 or i == 7:
#         continue
#     if i == 15:
#         break
#     print(i)

# sum = 0
# for i in range(1, 51):
#     sum += i
# print(f"The sum of numbers from 1 to 50 is: {sum}")


# sum=0
# list1=[]
# for i in range(1,11):
#     list1.append(i)
#     sum += i
# print(f"The list of numbers from 1 to 10 is: {list1}")
# print(f"The sum of numbers from 1 to 10 is: {sum}") 

# n=1
# list=['Nanded', 'Pune', 'Mumbai', 'Nagpur', 'Delhi']
# for i in list:
#     print(f"{n}. {i}")
#     n += 1
    
    
# 2.While Loop.

# Definition: A while loop keeps running the code while a given condition is true.

# Real-Life Example
#     ==>Think of a mobile charging:
#     ==>While the battery is less than 100%, keep charging.
#     ==>When it reaches 100%, stop charging.

# Syntax :
# while condition:
#     # code block to be executed


# num = 1
# while num<=10:
#     print(f"{num}-->Hello World.")
#     num += 1
    
# num = 0
# while num<=15:
#     num += 1
#     if num == 5:
#         # num += 1
#         break
#     print(f"{num} Hello World.")

# num = 1
# sum = 0
# while num<=50:
#     sum += num
#     num += 1
# print(f"The sum of numbers from 1 to 50 is: {sum}")


# # 1.WAP to print numbers from 10 to 1 using while loop.
# num = 10
# while num>=1:
#     print(f"The number is: {num}")
#     num -= 1
    
# # 2.WAP to reverse a given number using while loop.
# num = int(input("Enter a number to reverse(4 digit number): "))
# reverse = 0
# while num >= 1:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print(f"The reversed number is: {reverse}")

# # 3.WAP to print the table of given number.
# num = int(input("Enter a number to print its table: "))
# count = 1
# while count <= 10:
#     result = count * num
#     print(f"{num} x {count} = {result}")
#     count += 1
    
# num = int(input("Enter a number for finding the cube of these number: "))
# cube = 0
# while num >= 1:
#     digit = num % 10
#     cube = digit**3
#     num = num//10
#     print(f"The cube of {digit} is: {cube}")

# num = int(input("Enter a number for finging square of these number: "))
# square = 0
# while num >= 1:
#     digit = num % 10
#     square = digit**2
#     num = num//10
#     print(f"{digit} square is : {square}")