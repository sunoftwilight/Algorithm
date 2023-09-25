T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())

    k = N // P
    m = N % P

    max_s = k ** (P - m)

    if m != 0:
        max_s *= ((k + 1) ** m)

    print(f'#{tc} {max_s}')
