def solution(order):
    answer = 0
    for i in order:
        if i in ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]:
            answer += 5000
        elif i in ["hotamericano", "americanohot", "iceamericano", "americanoice", "americano", "anything"]:
            answer += 4500
    return answer
