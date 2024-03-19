def solution(strArr):
    answer = []
    for i, s in enumerate(strArr):
        if i % 2 == 0:  # 짝수 인덱스인 경우
            answer.append(s.lower())
        else:  # 홀수 인덱스인 경우
            answer.append(s.upper())
    return answer