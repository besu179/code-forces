t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map( int, input().split()))
    is_possible = True
    
    for i in range(n):
        for j in range(n - i -1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) > 1:
            is_possible = False
    if is_possible:
        print("YES")
    else:
        print('NO')