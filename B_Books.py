n, t = map(int, input().split())
a = list(map(int, input().split()))

l = ans = curr_sum = 0

for r in range(len(a)):
    curr_sum += a[r]
    
    while curr_sum > t:
        curr_sum -= a[l]
        l += 1
    ans = max(r - l + 1, 1)
print(ans)