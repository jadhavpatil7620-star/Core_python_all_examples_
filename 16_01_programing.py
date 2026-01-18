# # WAP to check graeter number among three numbers
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# if num1>num2:
#     if num1 > num3:
#         print(f"{num1} is greater than {num2} and {num3}.")
#     # else:
#         # print(f"{num2} is greater than {num1} and {num3}.")
# else:
#     if num3>num1:
#         print(f"{num3} is greater than {num1} and {num2}.")
#     else:
#         print(f"{num2} is greater than {num1} and {num3}.")

print("#####################################################################################################################################")   
        
# # Nasted For loop:
# for i in range(21,31):
#     print(f"The range of 21 to 31 is: {i}")

# Print * using one for loop:
# for i in range(5):
#     print("* * * * *")
    
# Print * using nasted for loop:
# for i in range(5):
#     for j in range(i):
#         print()
        
# for i in range(5):
#     print("* " * (i+1))

# for i in range(5):
#     print("1 " * (i+1))

# for i in range(5):
#     for j in range(i+1):
#         print("1", end=" ")
#     print()
    
# for i in range(5):
#     for j in range(i+1):
#         print(i+1, end=" ")
#     print()
    
# for i in range(5):
#     for j in range(i+1):
#         print(j,end=" ")
#     print()
    
# HomeWork Problems:
#1
#2 3
#4 5 6
#7 8 9 10

num = 1
for i in range(1,5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()