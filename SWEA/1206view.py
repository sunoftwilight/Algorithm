# import sys; sys.stdin = open('view_input.txt')

for test_case in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))

    get_sun = 0

    for i in range(2, N-2):
        # max_around = max(heights[i-2], heights[i-1], heights[i+2], heights[i+1])
        max_around = 0
        for k in range(5):
            if k != 2 and max_around < heights[i-2+k]:
                max_around = heights[i-2+k]

        if heights[i] > max_around :
            get_sun += (heights[i]-max_around)

    print(f'#{test_case} {get_sun}')