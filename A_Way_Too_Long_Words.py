num_words = int(input())
for _ in range(num_words):
    txt = input().lower()
    if len(txt) <= 10:
        print(txt)
    else:
        print(f"{txt[0]}{len(txt) - 2}{txt[-1]}")
