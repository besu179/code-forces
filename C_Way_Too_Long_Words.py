t = int(input())

for i in range(t):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        length = len(word)
        print(f"{word[0]}{length - 2}{word[-1]}")
