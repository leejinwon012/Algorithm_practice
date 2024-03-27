def solution(numLog):
    answer = ''
    for i in range(len(numLog) - 1):
        gap = numLog[i+1] - numLog[i]
        if gap == 1:
            answer += 'w'
        elif gap == -1:
            answer += 's'
        elif gap == 10:
            answer += 'd'
        elif gap == -10:
            answer += 'a'
    return answer