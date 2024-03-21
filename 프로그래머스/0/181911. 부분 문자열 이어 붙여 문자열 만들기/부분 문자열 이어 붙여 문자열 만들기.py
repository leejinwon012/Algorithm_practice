def solution(my_strings, parts):
    answer = []
    for i in range(len(my_strings)):
        string = my_strings[i]
        start, end = parts[i]
        answer.append(string[start:end+1])
    return ''.join(answer)