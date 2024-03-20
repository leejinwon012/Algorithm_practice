idx = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:  # 입력이 모두 0인 경우 종료
        break

    result = 0
    # 캠핑 가능한 일 수 계산
    result += (v // p) * l
    result += min(v % p, l)  # 남은 일 수 중 l일 이하인 경우 추가 캠핑 가능
    print(f'Case {idx}: {result}')
    idx += 1
