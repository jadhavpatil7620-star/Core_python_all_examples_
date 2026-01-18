# Level 1

mi={}

mi[45]="Rohit Sharma"

mi[33]="Hardik Pandya"

mi[93]="Jasprit Bumrah"

mi[63]="Surya Kumar Yadav"

mi[18]="Ishan Kishan"

# print("Original Dictionary:",mi)

# print(f"Name of player with jersey number 33: {mi[33]}")

# mi[45]="Captain Rohit Sharma"

# print("Updated Dictionary:",mi)

# print("Jersey numbers in the team:",list(mi.keys()))

# print("Player names in the dictionary:",list(mi.values()))

# for player in mi:
#     print(f"Jersey Number:{player} Player Name:{mi[player]}")



# Level 1.5

# print("Total Players in the team:",len(mi))
# print(f"There are {len(mi)} players in the team with jersey number=")
# for jersey_no in mi:
#     print(jersey_no)

# count=0
# print(f"These are the players whose names carry 'Y' later in their names:")
# for i in mi:
#     if 'y'in mi[i] or 'Y' in mi[i]:
#         print(mi[i])
#         count+=1
# print(count)

count=0
print("These are the players whose names are longer than 12 characters:")
for i in mi:
    if size:=len(mi[i])>12:
        print(mi[i])
        count+=1
print(count)

print("These are the players whose names end with 'a':")
for i in mi:
    if End:=mi[i].endswith('a'):
        for ch in mi[i]:
            print(ch)
            
            
