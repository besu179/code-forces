num_of_cards = int(input())
cards = input().split()
cards_int = [int(card) for card in cards]

pt1 = 0
pt2 = 0
turn = 0

while cards_int:
    if cards_int[0] >= cards_int[-1]:
        big = cards_int.pop(0)
    else:
        big = cards_int.pop()
    
    if turn == 0:
        pt1 += big
    else:
        pt2 += big
        
    turn = 1 - turn
        
print(pt1, pt2)