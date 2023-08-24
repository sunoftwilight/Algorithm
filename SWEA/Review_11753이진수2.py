def solve(n):
    rst = ''
    cnt = 0

    while n and cnt < 13:
        n *= 2
        cnt += 1

        # 2를 곱한 값이 1 이상일 때
        if n >= 1:
            rst += '1'
            n -= 1      # 소수점 아래만 필요

        else:
            rst += '0'

    if cnt >= 13:
        return 'overflow'
    else:
        return rst


T = int(input())

for tc in range(1, T+1):
    N = float(input())

    print(f'#{tc} {solve(N)}')
