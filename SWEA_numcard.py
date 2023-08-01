T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = input()

    cnt = [0] * 10

    for i in num:
        cnt[int(i)] += 1

    many = 0
    idx = 0

    for k in range(10):
        if cnt[k] >= many :
            many = cnt[k]
            idx = k

    print(f'#{tc} {idx} {many}')