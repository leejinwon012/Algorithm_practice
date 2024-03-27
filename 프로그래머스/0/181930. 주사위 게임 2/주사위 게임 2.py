def solution(a, b, c):
    total = a + b + c
    if a == b == c:
        return total * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or b == c or a == c:
        return total * (a**2 + b**2 + c**2)
    return total