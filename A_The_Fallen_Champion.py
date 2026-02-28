w, t = map(int, input().split())

n = int(input())

is_winner = False

for _ in range(n):
    win, time = map(int,input().split())
    if win > w:
        is_winner = True
        break
    elif win == w and time < t:
        is_winner = True
        break
if is_winner:
    print("The Fallen Champion")
else:
    print("The Champion Saves the Accused")
    