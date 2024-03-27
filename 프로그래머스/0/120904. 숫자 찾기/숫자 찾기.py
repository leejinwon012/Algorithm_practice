def solution(num, k):
    num_str = str(num)
    for i in range(len(num_str)):
        if int(num_str[i]) == k:
            return i+1
    return -1