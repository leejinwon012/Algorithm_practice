def solution(my_string, s, e):
    sub_str = my_string[s:e+1][::-1]
    return my_string[:s] + sub_str + my_string[e+1:]