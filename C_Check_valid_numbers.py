test_num = int(input()) 
for i in range(test_num):
    n, m, p, q = map(int, input().split())
    
    
    if n % p == 0:
        if m == (n // p) * q:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
