t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    swaps = 0
    j = 0
    
    for i in range(n - 1):
        if s[i] == "A" and s[i+ 1] == "B":
            swaps += j +1
            s[i + 1] = "A"
            j = 0
        elif s[i] == "A":
            j += 1
        elif s[i] == "B":
            j = 0
    print(swaps)