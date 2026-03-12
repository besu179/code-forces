num_of_cards = int(input())
cards = list(map(int, input().split()))

pt1 = 0
pt2 = 0
turn = 0

while cards:
    if cards[0] >= cards[-1]:
        big = cards.pop(0)
    else:
        big = cards.pop()
    
    if turn == 0:
        pt1 += big
    else:
        pt2 += big
        
    turn = 1 - turn
        
print(pt1, pt2)