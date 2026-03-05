t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    ans = a[n-1] - a[0]
    
    start_index = 0
    while (start_index + 2) < n:
        diff = a[start_index + 2] - a[start_index]
        if diff < ans:
            ans = diff
        start_index += 1
        
    print(ans)
