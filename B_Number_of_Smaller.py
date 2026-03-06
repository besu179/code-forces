n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
ans = []

for j in range(m):
    while i < n and a[i] < b[j]:
        i += 1
    ans.append(i)

print(*ans)
