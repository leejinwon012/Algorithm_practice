def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])

    sorted_string = sorted(answer)
    return sorted_string