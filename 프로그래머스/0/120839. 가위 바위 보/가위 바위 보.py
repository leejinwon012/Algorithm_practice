def solution(rsp):
    answer = []         # " " 문자열엔 append 사용이 불가능해서 answer을 리스트로
    for i in rsp:
        if i in "2":
            answer.append('0') 
        elif i in "0":
            answer.append('5')
        elif i in "5":
            answer.append('2')

    answer = "".join(answer)        # join 함수 개념 확실히!
    return answer