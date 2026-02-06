friends = int(input())
lst = input().split()

for i in lst:
    if i != friends:
        print(lst[i], end=" ")