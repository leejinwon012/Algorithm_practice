n = int(input())

for i in range(1, n + 1):
    t = input()
    if t == t[::-1]:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")