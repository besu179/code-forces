test_cases = int(input())

for i in range(test_cases):
    ans = 0
    n = int(input())
    if n > 3 and n % 2 == 0:
        ans = (n // 2) - 1
    else:
        ans = n // 2
    if n == 1 or n == 2:
        ans = 0
    print(ans)