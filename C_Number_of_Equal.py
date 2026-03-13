import sys

input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
a = list(map(int, data[2 : n + 2]))
b = list(map(int, data[n + 2 : ]))

i = j = ans = 0

while i < n and j < m:
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        target = a[i]
        
        cnt1 = 0
        while i < n and a[i] == target:
            cnt1 += 1
            i += 1
            
        cnt2 = 0
        while j < m and b[j] == target:
            cnt2 += 1
            j += 1
            
        ans += (cnt1 * cnt2)

print(ans)
