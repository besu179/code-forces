n, s = map(int, input().split())
a = list(map(int, input().split()))

max_len = cur_sum = l = 0

for r in range(n):
    cur_sum += a[r]
    
    while cur_sum > s:
        cur_sum -= a[l]
        l += 1
    max_len = max(max_len, r - l + 1)
    
print(max_len)