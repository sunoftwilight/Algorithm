import heapq

N = int(input())

time = []
for _ in range(N):
    s, t = map(int, input().split())
    time.append([s, t])

time2 = sorted(time)
print(time2)
time.sort(key=lambda x:x[1])
print(time)

end_class = []
heapq.heappush(end_class, time[0][1])

for i in range(1, N):
    if time[i][0] < end_class[0]:
        heapq.heappush(end_class, time[i][1])
    else:
        heapq.heappop(end_class)
        heapq.heappush(end_class, time[i][1])

print(len(end_class))
