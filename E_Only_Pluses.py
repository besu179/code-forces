t = int(input())
for i in range(t):
    nums= [int(x) for x in input().split()]
    for _ in range(5):
        index = nums.index(min(nums))
        nums[index] += 1
    ans = 1
    for num in nums:
        ans *= num
    print(ans)