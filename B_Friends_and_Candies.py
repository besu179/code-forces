test_case = int(input())
for i in range(test_case):
    len_arr = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    ans = 0

    if total_sum % len_arr == 0:
        avg = total_sum // len_arr
        for num in arr:
            if num > avg:
                ans += 1
        print(ans)
    else:
        print(-1)
