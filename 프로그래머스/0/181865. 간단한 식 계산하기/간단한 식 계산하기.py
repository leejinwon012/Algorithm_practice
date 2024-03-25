def solution(binomial):
    numbers = []

    for i in binomial.split():
        if i.isdigit():         # 분리된 문자열 숫자로 리턴
            numbers.append(int(i))

    if '+' in binomial:
        return numbers[0] + numbers[1]
    elif '-' in binomial:
        return numbers[0] - numbers[1]
    elif '*' in binomial:
        return numbers[0] * numbers[1]
