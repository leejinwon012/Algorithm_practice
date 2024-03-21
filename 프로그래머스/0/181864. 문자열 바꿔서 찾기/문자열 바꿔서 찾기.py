def solution(myString, pat):
    b_temp = myString.replace("A", "b_temp")
    a_temp = b_temp.replace("B", "a_temp")
    final_string = a_temp.replace("b_temp", "B").replace("a_temp", "A")

    if pat in final_string:
        return 1
    else:
        return 0