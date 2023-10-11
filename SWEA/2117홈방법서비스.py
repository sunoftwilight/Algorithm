cost = [(k * k) + (k - 1) * (k - 1) for k in range(40)]
#
# def solve():
#     ans = 0
#
#     for si in range(N):
#         for sj in range(N):      # 모든 시작 위치에 대해 처리 (si, sj는 마름모의 중앙
#             for k in range(1, 2 * N):    # 가로 세로 모두 확장해도 2*N
#                 cnt = 0
#                 for i in range(si - (k - 1), si + k):
#                     for j in range(sj - (k - 1) + abs(i - si), sj + k - abs(i - si)):     # (si, sj) 기준으로 상하좌우로 마름모 뻗어가기
#                         if 0 <= i < N and 0 <= j < N and arr[i][j]:          # 범위 내이고 집이면
#                             cnt += 1
#
#                 # cost = k * k + (k - 1) * (k - 1)
#                 # 비용보다 수익이 많고,현재 ans보다 더 많은 집 방범하면 갱신
#                 if cost[k] <= cnt * M and ans < cnt:
#                     ans = cnt
#     return ans
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     print(f'#{tc} {solve()}')

def solve2():
    ans = 0

    # home 배열 생성
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append((i, j))

    # 모든 좌표 순회하며 dist 배열 만들고, cnt 세기
    for si in range(N):
        for sj in range(N):
            dist = [0] * 40
            for hi, hj in home:
                t = abs(si - hi) + abs(sj - hj) + 1
                dist[t] += 1

            cnt = 0
            for k in range(1, 40):
                cnt += dist[k]
                if cost[k] <= cnt * M and ans < cnt:
                    ans = cnt

    return ans


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {solve2()}')
