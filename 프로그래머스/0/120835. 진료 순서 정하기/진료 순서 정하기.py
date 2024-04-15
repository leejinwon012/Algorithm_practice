def solution(emergency):
    answer = []
    nw_emergency = sorted(emergency, reverse=True)

    for i in emergency:
        answer.append(nw_emergency.index(i)+1)
    return answer