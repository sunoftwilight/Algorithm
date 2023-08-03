def binary_search(n, Ps):
    left = 1
    right = n
    cnt = 0

    while left <= right:
        mid = (left + right) // 2

        if mid == Ps:
            cnt += 1
            return cnt

        elif mid > Ps:
            right = mid
            cnt += 1

        else:
            left = mid
            cnt += 1


T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = list(map(int, input().split()))

    cnt_a = binary_search(P, Pa)
    cnt_b = binary_search(P, Pb)

    if cnt_a < cnt_b:
        ans = 'A'

    elif cnt_b < cnt_a:
        ans = 'B'

    else:
        ans = 0

    print(f'#{tc} {ans}')
