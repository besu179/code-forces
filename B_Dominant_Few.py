t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    ans = False
    mid = (n // 2)
    
    if n % 2:
        i = mid
        j = mid
        #even
    else:
        i = mid
        j = mid - 1
        #odd
    if sum(a[:j]) > sum(a[i:]):
        ans = True
    
    print("YES") if ans else print("NO")