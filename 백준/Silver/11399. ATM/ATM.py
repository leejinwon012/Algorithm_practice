n = int(input())
time = list(map(int, input().split()))
time.sort()
total_time = 0

for i in range(n):
    total_time += sum(time[:i+1])
print(total_time)