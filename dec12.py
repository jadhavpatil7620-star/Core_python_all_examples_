l=[]
print(type(l),"\n",l,"\n",id(l))
l.append("Gopal")
l.append(20)
l.append(20.25)
l.append("Jadhav")
# print(l,"\n",len(l))
l.insert(0,"12abc")
# print(l)
# res=l[4]
# print(res.count("a"))
# print(l[4][2:])
for i in l:
    print(i)
    
l.append(["My name is Gopal Jadhav"])
print(l)
print(l[5][0].split())
# print(s.split())