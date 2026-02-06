test = int(input())

for _ in range(test):
    n_of_monsters, k_bullet = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    monsters = []

    for i in range(n_of_monsters):
        monsters.append((abs(x[i]), a[i]))

    monsters.sort()

    total_health = 0
    can_survive = True

    for distance, health in monsters:
        total_health += health

        if total_health > distance * k_bullet:
            can_survive = False
            break

    if can_survive:
        print("YES")
    else:
        print("NO")
