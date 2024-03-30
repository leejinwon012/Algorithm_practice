def solution(str1, str2):
    answer = ''
    list(str1), list(str2)
    for i in range(len(list(str1))):
        answer += list(str1)[i] + list(str2)[i]
    return answer