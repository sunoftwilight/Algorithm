T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))

    max_height = 0

    for i in range(N):
        this_height = N - 1 - i

        for k in range(i+1, N):
            if heights[i] <= heights[k]:
                this_height -= 1

        if max_height < this_height:
            max_height = this_height

    print(f'#{test_case} {max_height}')