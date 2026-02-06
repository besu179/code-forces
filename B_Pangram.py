count = int(input())
txt = input().lower()

if count <= 25 or len(set(txt)) <= 25:
    print("NO")
else:    
    print("YES")