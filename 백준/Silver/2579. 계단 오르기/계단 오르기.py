n = int(input())
data = [0]
for _ in range(n):
    data.append(int(input()))

dp = [0] * (n + 1)      # 최대 합 저장
dp[1] = data[1]         # 첫 번째 원소는 그 자체로 최대 합이므로 초기화
if n > 1:
    dp[2] = data[1] + data[2]   # 두 번째 원소까지 고려해서 최대 합을 구해야 하므로 초기화

for i in range(3, n + 1):
    # i를 선택하는 경우 - 이전의 연속된 원소들과 i번째 원소를 선택하여 최대 합을 구함
    # i를 선택하지 않는 경우 - 이전의 연속된 원소들 중에서 i - 1번째 원소까지 선택한 후, i번째 원소를 선택함
    dp[i] = max(dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])

print(dp[n])