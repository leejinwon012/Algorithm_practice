def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code): # range(start, end, gap)
        answer += cipher[i]
    return answer