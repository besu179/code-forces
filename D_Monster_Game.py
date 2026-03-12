t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort(reverse=True)
    
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + b[i]
    
    max_score = 0
    L = 0  
    
    for i in range(n):
        num_swords = i + 1
        difficulty = a[i]
        
        while L < n and pref[L+1] <= num_swords:
            L += 1
            
        max_score = max(max_score, difficulty * L)
        
    print(max_score)
