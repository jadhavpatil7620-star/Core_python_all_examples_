# r=range(1,11)
# print(type(r))    # <class 'range'>
# print(r)    # range(1, 11)
# l=list(r)
# print(type(l))  #<class 'list'>
# print(l)      # [1,2,3,4,5,6,7,8,9,10]
# for i in r:
#     print(i)    # 1,2,3,4,5,6,7,8,9,10
    
    
    
# print(sum(r))   # 55



# r=range(0,51,5)
# print(type(r))   # <class 'range'>
# print(r)    # range(0, 51, 5)
# for i in r:
#     print(i)  # 0,5,10,.....,50
# l=list(r)
# print(l)  # [0,5,10,....,50]


# a=range(100,151,10)
# for i in a:
#     print(i)   # 100,110,120,130,140,150
# b=list(a)
# print(b)     # [100,110,120,130,140,150]



# c=range(2,21,-2) 
# print(c)   # invalid range as step is negative but start<end



# d=range(20,1,-2)
# for i in d:
#     print(i)   # 20,18,16,14,12,10,8,6,4,2
    
    
    
    
# r2=range(0,-10,-1)
# for i in r2:
#     print(i)  # 0,-1,-2,-3,-4,-5,-6,-7,-8,-9
# l2=list(r2)
# print(l2)   # [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]





# for i in range(19,191,19):
#     print(f"19 *  {i}")   # 19,38,57,76,95,114,133,152,171,190
    
# l3=list(range(19,191,19))
# print(l3)   # [19,38,57,76,95,114,133,152,171,190]

# num=eval(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")   # multiplication table of 5

    # print("{0} * {1} = {2}".format(num,i,num*i))
    
    
    
    
# s="Gopal Jadhav"
# for i in range(0,len(s)):
#     print(s[i])   # G,o,p,a,l, ,J,a,d,h,a,v
    
    
# s1="Instagram"
# for i in range(0,len(s1)):
#     if i%2==1:
#         print(i,"------------>",s1[i])   # 0->I,2->s,4->a,6->r,8->m
        
        
# lst=[1,2,"Gopal",4.5,"Jadhav",True]
# for i in range(0,len(lst)):
#     print(i)   # 0,1,2,3,4,5
#     if i%2==0:
#         print(i,"------>",lst[i])   # 0->1,2->Gopal,4->Jadhav
        
        
# tpl=(10,20,30,"Gopal",40.5,"Jadhav",False)
# for i in range(0,len(tpl)):
#     if i%2==1:
#         print(i,"------>",tpl[i])   # 1->20,3->Gopal,5->Jadhav
        
        
        
# L=[20,30,40,50,60]
# for i in range(len(L)-1,-1,-1):
#     print(L[i])   # 60,50,40,30,20
    
    
    
    
l2=[23,25,63,45,12,78,90]
chotu_sq_list=[]
chotu_cube_list=[]
for i in range(len(l2)):
    if i%2==0:
        chotu_sq_list.append(l2[i]**2)
    else:
        chotu_cube_list.append(l2[i]**3)
print("Original List:",l2)   # [23,25,63,45,12,78,90]
print("Chotu Square List:",chotu_sq_list)   # [529, 3969, 144, 8100]
print("Chotu Cube List:",chotu_cube_list)   # [15625, 91125, 474552, 729000]