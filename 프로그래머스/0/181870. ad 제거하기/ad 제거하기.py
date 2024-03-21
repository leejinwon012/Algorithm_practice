def solution(strArr):
    result = []
    for i in strArr:
        if 'ad' not in i:   # 문자열 반복동안 해당 리스트 수정은 안하는게 좋음
            result.append(i)
    return result