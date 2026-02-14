num_words = int(input())
for _ in range(num_words):
    txt = input()
    print(txt if len(txt) < 10 else f"{txt[0]}{len(txt) - 2}{txt[-1]}")
