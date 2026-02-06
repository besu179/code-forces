password = input() #ya
num_of_combinations = int(input()) #4
txt = [] # empty list
for i in range(num_of_combinations): 
    txt.append(input())
found = False 
for i in range (num_of_combinations): #0
    for j in range(num_of_combinations): # 1
        if password in txt[i] + txt[j]: # ah + oy 
            found = True
            break
    if found:
        break

if found:
    print("YES")
else:
    print("NO")
    