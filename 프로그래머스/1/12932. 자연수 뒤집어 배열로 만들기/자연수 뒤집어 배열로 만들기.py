def solution(n):
    answer = []
    n = list(map(int,str(n)))
    for i in n[::-1]:
        answer.append(i)
    return answer