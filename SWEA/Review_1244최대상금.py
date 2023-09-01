'''
Ex > num = 123, N = 3이면,
num에 대해 위치 3회까지 자리 변경했을 때 가능한 모든 케이스를 확인하며,
가장 큰 숫자를 찾으면 그것이 정답이다!!

+) 123 --(int to ascii)--> 1 2 3 --(swqp)--> 2 1 3 --(ascii to int--> 213
'''


def swap(prize, i, j):             # 123 -> |1|2|3| -> |2|1|3|
    # int to ascii (itoa)
    prize_arr = [0] * prize_len
    for k in range(prize_len-1, -1, -1):
        prize_arr[k] = prize % 10
        prize //= 10

    # swap
    prize_arr[i], prize_arr[j] = prize_arr[j], prize_arr[i]

    # ascii to int (atoi)
    prize = 0
    for k in range(prize_len):
        prize = prize * 10 + prize_arr[k]

    return prize


def find_max(n, k, prize):     # 123
    global ans

    # 메모이제이션 + 가지치기
    for i in range(720):
        if memo[k][i] == 0:
            memo[k][i] = prize
            break

        elif memo[k][i] == prize:
            return


    if n == k:
        ans = max(ans, prize)

    else:
        for i in range(prize_len - 1):                  # nC2
            for j in range(i+1, prize_len):
                find_max(n, k+1, swap(prize, i, j))     # 213


def get_length(prize):                                  # 숫자판 길이 구하기
    cnt = 0

    while prize:
        prize //= 10
        cnt += 1

    return cnt


T = int(input())

for tc in range(1, T+1):
    prize, N = map(int, input().split())                # 숫자판, 교환 횟수

    memo = [[0] * 720 for _ in range(N+1)]              # 메모이제이션
    prize_len = get_length(prize)
    ans = 0

    find_max(N, 0, prize)     # find_max(swap 횟수, k(=가지의 depth), 상금)

    print(f'#{tc} {ans}')
