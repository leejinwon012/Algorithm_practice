n = int(input())
num_list = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(0, i):
        if num_list[i] < num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

# dp[n-1]로 했더니 오류
# why? dp 배열에서 항상 뒤에서 첫번째 오는 값이 최댓값이라는 보장이 없음
print(max(dp))