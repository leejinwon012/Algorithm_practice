def solution(n_str):
    for index, i in enumerate(n_str):
        if i != '0':
            return n_str[index:]
    return n_str