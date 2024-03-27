def solution(age):
    answer = ''
    new_age = ['a','b','c','d','e','f','g','h','i','j']
    # index = 0 1 2 3 4 5 6 7 8 9
    for i in str(age):
        answer += new_age[int(i)]
    return answer