def solution(myStr):
    new_str = myStr.replace("a", " ").replace("b", " ").replace("c", " ")
    answer = new_str.split()

    if answer:
        return answer
    else:
        return ["EMPTY"]
