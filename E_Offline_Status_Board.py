t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    idx_a = {val: i for i, val in enumerate(a)}
    
    res = 0
    last_idx = n
    
    for i in range(n - 1, -1, -1):
        cur_b = b[i]
        cur_b_in_a_idx = idx_a[cur_b]
        
        if cur_b_in_a_idx < last_idx:
            res += 1
            last_idx = cur_b_in_a_idx
        else:
            break
            
    print(n - res)
