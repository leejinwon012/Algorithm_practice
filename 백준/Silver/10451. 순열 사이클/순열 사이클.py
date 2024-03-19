from collections import deque

T = int(input())

def bfs(index):
    queue = deque()
    queue.append(index)
    while queue:
        cur = queue.popleft()
        visited[cur] = True
        if visited[graph[cur]] == False:
            visited[graph[cur]] = True
            queue.append(graph[cur])


for i in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    count = 0
    for j in range(1,n+1):
        if visited[j] == False:
            bfs(j)
            count += 1

    print(count)