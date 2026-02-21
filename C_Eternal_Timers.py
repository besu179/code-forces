t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = True
    for i in range(n):
        if arr[i] <= 2 * max(i, n - 1 - i):
            ans = False
            break
    
    print("YES" if ans else "NO")