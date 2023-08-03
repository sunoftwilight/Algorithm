# import sys
# sys.stdin = open("input (1).txt", "r")
def min_max(box, N):
    max_idx = min_idx = 0

    for i in range(1, N):
        if box[max_idx] < box[i]:
            max_idx = i

        if box[min_idx] > box[i]:
            min_idx = i

    return max_idx, min_idx


T = 10

for tc in range(1, T+1):
    dump_cnt = int(input())                # dump 횟수
    N = 100
    box = list(map(int, input().split()))

    for _ in range(dump_cnt):
        max_idx, min_idx = min_max(box, N)
        box[max_idx] -= 1
        box[min_idx] += 1

    max_idx, min_idx = min_max(box, N)
    print(f'#{tc} {box[max_idx]-box[min_idx]}')
