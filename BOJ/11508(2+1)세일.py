import heapq
N = int(input())

cost = []
for _ in range(N):
    heapq.heappush(cost, -int(input()))

pay_N = N // 3
total_pay = 0

for _ in range(pay_N):
    exp1, exp2, chp = heapq.heappop(cost), heapq.heappop(cost), heapq.heappop(cost)
    total_pay += exp1 + exp2

# for i in range(len(cost)):
#     total_pay += cost[i]
total_pay += sum(cost)
print(-total_pay)

# N = int(input())
#
# cost = []
# for _ in range(N):
#     cost += [int(input())]
#
# cost.sort(reverse=True)
#
# pay_N = N // 3
# total_pay = 0
#
# i = 0
# for _ in range(pay_N):
#     bundle = cost[i:i+3]
#     total_pay += bundle[0] + bundle[1]
#     i += 3
#
# for j in range(i, N):
#     total_pay += cost[j]
#
# print(total_pay)
