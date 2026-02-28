n, k = map(int, input().split())

odds = (n + 1) // 2

if odds >= k:
    print((k * 2) - 1)
else:
    print((k - odds) * 2)