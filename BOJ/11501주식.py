T = int(input())

for tc in range(T):
    N = int(input())
    juga = list(map(int, input().split()))

    ans = 0
    # for i in range(N-1):
    #     max_aft = max(juga[i+1:])
    #     if juga[i] < max_aft:
    #         ans += max_aft - juga[i]
    max_v = 0
    for i in range(N-1, -1, -1):
        max_v = max(max_v, juga[i])
        if juga[i] < max_v:
            ans += max_v - juga[i]

    print(ans)
