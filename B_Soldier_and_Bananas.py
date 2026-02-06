inp = input().split(" ")
k = int(inp[0]) #cost of the first banana
n = int(inp[1]) #initial number of dollar
w = int(inp[2]) #number of banana he wants
total = 0
for i in range(1, w + 1 ):
    total += i * k
if total > n:
    print(total - n)
else:
    print(0)