n = int(input())
count = {}
is_lady = False

for _ in range(n):
    m = int(input())
    for _ in range(m):
        s, h = input().split()
        count[(s, h)] = count.get((s, h), 0) + 1

for val in count.values():
    if (val / n) * 100 >= 80:
        is_lady = True
        break

print("YES") if is_lady else print("NO")
