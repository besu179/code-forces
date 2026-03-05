from collections import Counter
t = int(input())

for _ in range(t):
    n  = int(input())
    a = Counter(map(int, input().split()))
    
    mx = False
    
    for value in a.values():
        if value % 2:
            mx = True
            break
    
    print("YES") if mx else print('NO')