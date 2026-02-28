t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    current_max = max(a)
    
    ans = []
    for _ in range(m):
        op = input().split()
        min_num = int(op[1])
        max_num = int(op[2])
        
        if current_max >= min_num and current_max <= max_num:
            if op[0] == "+":
                current_max += 1
            else:
                current_max -= 1
        
        ans.append(str(current_max))
        
    print(" ".join(ans))
