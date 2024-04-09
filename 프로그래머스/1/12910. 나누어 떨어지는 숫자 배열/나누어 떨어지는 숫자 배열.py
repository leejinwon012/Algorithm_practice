def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    return sorted(answer) if answer else [-1]   # 삼항 표현식