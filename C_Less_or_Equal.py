n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if k == 0:
    if arr[k] > 1:
        ans = 1
    else:
        ans = -1
elif k == n:
    ans = arr[k - 1]
else:
    if arr[k - 1] == arr[k]:
        ans = -1
    else:
        ans = arr[k - 1]
print(ans)