def solution(strArr):
    # 문자열 길이를 카운트할 딕셔너리 생성
    length_counts = {}

    # 각 문자열의 길이를 카운트
    for s in strArr:
        length = len(s)
        if length in length_counts:
            length_counts[length] += 1
        else:
            length_counts[length] = 1

    # 문자열 길이의 최댓값 찾기
    max_length = max(length_counts, key=length_counts.get)

    # 최댓값에 해당하는 문자열 개수 반환
    max_group_size = length_counts[max_length]

    return max_group_size

