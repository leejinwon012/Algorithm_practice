def solution(rsp):
    answer = []
    for i in rsp:
        if i in "2":
            answer.append('0')
        elif i in "0":
            answer.append('5')
        elif i in "5":
            answer.append('2')

    answer = "".join(answer)
    return answer