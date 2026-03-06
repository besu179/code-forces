m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []

i = 0
j = 0

while i < m and j < n:
    if a[i] <= b[j]:
        ans.append(a[i])
        i += 1
    else:
        ans.append(b[j])
        j += 1
        
while i < m:
    ans.append(a[i])
    i += 1

while j < n:
    ans.append(b[j])
    j += 1
    
print(" ".join(map(str, ans)))
