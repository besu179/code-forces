password = input().strip()
n = int(input())

words = set()
for _ in range(n):
    words.add(input().strip())

found = False

for w in words:
    if password.startswith(w):
        rest = password[len(w):]
        if rest in words:
            found = True
            break
if found:
    print("YES")
else:
    print("NO")
