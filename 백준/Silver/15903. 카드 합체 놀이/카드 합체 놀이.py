import heapq

n,m = map(int,input().split())
status = list(map(int,input().split()))

heapq.heapify(status) # 초기 카드 리스트를 최소 힙으로 변환

for _ in range(m):
    # 현재 가장 작은 두 카드를 추출
    small1 = heapq.heappop(status)
    small2 = heapq.heappop(status)

    # 현재 가장 작은 두 카드를 추출
    heapq.heappush(status, small1 + small2)
    heapq.heappush(status, small1 + small2)

print(sum(status))

