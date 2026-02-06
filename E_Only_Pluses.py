t = int(input())
for i in range(t):
    nums = [int(x) for x in input().split()]

    for _ in range(5):
        idx = nums.index(min(nums))
        nums[idx] += 1

    val = 1
    for num in nums:
        val *= num
    
    print(val)
