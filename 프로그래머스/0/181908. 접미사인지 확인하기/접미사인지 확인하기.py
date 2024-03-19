def solution(my_string, is_suffix):
    if len(my_string) < len(is_suffix):
        return 0

    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            return 1
    return 0