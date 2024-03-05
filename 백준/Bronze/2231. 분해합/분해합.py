def answer(n):
    for i in range(1, n+1):
        digit = i + sum(map(int, str(i)))
        if digit == n:
            return i
    return 0

n = int(input())
solution = answer(n)
print(solution)