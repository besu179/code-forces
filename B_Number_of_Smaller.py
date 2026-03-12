n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
ans = []

for j in range(len(b)):
    while i < n and a[i] < b[j]:
        i += 1
    ans.append(i)

<<<<<<< HEAD
print(*ans)
=======
print(*ans)
>>>>>>> 76b8af10fff94674c1f8b47e55e13fddd8132f7a
