test_cases = int(input())

for i in range(test_cases):
    n = int(input())
    print(n % 2 if n > 3 else n)