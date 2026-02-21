for r in range(1, 6):
    row = input().split()
    if "1" in row:
        ans = abs(2 - row.index("1")) + abs(3 - r)
        print(ans)