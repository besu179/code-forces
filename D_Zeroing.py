n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

subtracted = 0
i = 0

while i < n and k > 0:
    if a[i] - subtracted > 0:
        print(a[i] - subtracted)
        subtracted += (a[i] - subtracted) 
        k -= 1
    i += 1

for _ in range(k):
    print(0)
