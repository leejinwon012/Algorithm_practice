n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]  # 동전의 가치를 입력받음
a.sort(reverse=True)

answer = 0
for coin in a:
    if k // coin > 0:  # 현재 동전으로 거슬러 줄 수 있는 횟수를 계산
        answer += k // coin  # 현재 동전으로 거슬러 준 횟수를 더함
        k %= coin  # 현재 동전으로 거슬러 주고 남은 나머지를 계산

print(answer)
