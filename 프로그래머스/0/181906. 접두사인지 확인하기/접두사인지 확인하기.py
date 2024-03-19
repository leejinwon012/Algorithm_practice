def solution(my_string, is_prefix):
    if len(my_string) < len(is_prefix):  # 문자열이 접두사보다 짧으면 접두사가 될 수 없음
        return 0

    for i in range(len(is_prefix)):
        if my_string[i] != is_prefix[i]:  # 문자열이 일치하지 않는 경우
            return 0

    return 1  # 문자열이 모두 일치하는 경우