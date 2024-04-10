def solution(num_list):
    answer = 0

    for i in num_list:
        result = i
        while result != 1:
            if result % 2 == 0:
                result = result // 2
                answer += 1
            else:
                result = (result - 1) // 2
                answer += 1
        
    return answer