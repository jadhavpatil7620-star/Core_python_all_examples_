# n=1
# for i in range(1,4):
#     for j in range(3):
#         print(n*i, end=" ")
#     print()
    
# for i in range(4):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(n*i, end=" ")
#     print()


# n=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# for i in range(4,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(n,end=" ")
#         n+=1
#     print()

# n=10
# for i in range(1,5):
#     for j in range(i):
#         print(n,end=" ")
#         n-=1
#     print()
    

# WAP to print the following pattern:
# A
# B B
# C C C

# for i in range(65,68):
#     for j in range(i-64):
#         print(chr(i), end=" ")
#     print()
# n=1
# for i in range(3,0,-1):
#     for j in range(i):
#         print(n,end=" ")
#         n+=1
#     print()

# n=1
# for i in range(1,4):
#     for j in range(3):
#         print(i,end=" ")
#         # n+=1
#     print()
    
# n=1   
# for i in range(1,4):
#     for j in range(1,4):
#         print(i+j-1,end=" ")
#     print()


# for i in range(3,0,-1):
#     for j in range(1,6,2):
#         print(j,end=" ")
#     print()

# for i in range(3,0,-1):
#     for j in range(5,2,-1):
#         print(j,end=" ")
#     print()


n=3
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

# for i in range(1,4):
#     for j in range(i):
#         print("*",end=" ")
#     print()