'''
[2차원 배열]
2 1 2
5 8 5
7 2 2
=================
0행에서 0번째
1행에서 1번째
2행에서 2번째 선택
=> 0 1 2

이런 식으로 모든 경우의 수 확인  (순열)
0 1 2      -> 2 + 8 + 2 = 12
0 2 1      -> 2 + 5 + 2 = 9
1 0 2      -> 1 + 5 + 2 = 8
1 2 0      -> 1 + 5 + 7 = 13
2 0 1      -> 2 + 8 + 7 = 17
2 1 0      -> 2 + 5 + 2 = 9
이 중 최소 합은 (1, 0, 2)

★★★ 가지치기!!!
'''

def perm(n, k, sum):
    global ans

    if ans < sum : return
    # 가지치기 (ans보다 sum이 크면 이미 정답이 될 수 없음! -> 종료)
    # => 메모리/실행 시간 아낄 수 있음

    if n == k:
        # print(p, end=' ')
        sum = 0

        for i in range(n):
            sum += arr[i][p[i]]
        # print(sum)
        if ans > sum:
            ans = sum

        return    # 없어도 무관

    else:
        for i in range(k, n):
            p[k], p[i] = p[i], p[k]
            perm(n, k+1, sum + arr[k][p[k]])
            p[k], p[i] = p[i], p[k]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = list(range(N))
    ans = 98764321

    perm(N, 0, 0)     # 총 깊이 N이고 시작 깊이는 0

    print(f'#{tc} {ans}')
