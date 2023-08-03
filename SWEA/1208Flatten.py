# import sys
# sys.stdin = open("input (1).txt", "r")
T = 10

for tc in range(1, T+1):
    N = int(input())                         # dump 횟수
    box = list(map(int, input().split()))

    for _ in range(N):
        max_h = min_h = box[0]
        max_idx = min_idx = 0

        for i in range(len(box)):
            if box[i] > max_h:
                max_h = box[i]
                max_idx = i

            if box[i] < min_h:
                min_h = box[i]
                min_idx = i

        box[max_idx] = max_h - 1
        box[min_idx] = min_h + 1

    last_max = last_min = box[0]

    for j in range(len(box)):
        if box[j] > last_max:
            last_max = box[j]

        if box[j] < last_min:
            last_min = box[j]

    ans = last_max - last_min

    print(f'#{tc} {ans}')
