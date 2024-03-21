def solution(myString):
    answer = []
    length = 0

    for char in myString:
        if char == 'x':
            answer.append(length)
            length = 0
        else:
            length += 1

    answer.append(length)
    return answer