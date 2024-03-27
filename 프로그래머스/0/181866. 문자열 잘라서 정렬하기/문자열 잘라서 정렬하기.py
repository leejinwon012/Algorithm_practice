def solution(myString):
    answer = []
    for i in myString.split('x'):
        if i != '':
            answer.append(''.join(i))
    return sorted(answer)