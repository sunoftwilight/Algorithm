T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pri = list(map(int, input().split()))

    ans = 0

    for i in range((N-1) - 1):
