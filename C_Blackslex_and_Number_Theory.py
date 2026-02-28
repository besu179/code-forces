import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    min_val = min(arr)
    diff_gcd = 0
    
    for num in arr:
        if num != min_val:
            diff_gcd = math.gcd(num - min_val, diff_gcd)
    
    print(diff_gcd)