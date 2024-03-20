def dfs(current_min):
    if current_min >= min_area:
        return


    pass


import copy

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

direct = {
    1: [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
    5: [[(0, 1), (1, 0), (0, -1), (-1, 0)]]
}

min_area = 999999999
cctv = []

for i in range(N):
    for j in range(M):
        if info[i][j] in direct:
            cctv.append((info[i][j], i, j))

case = copy.deepcopy(info)

for locate in cctv:
    num, r, c = locate
    # case 배열에 각 cctv별 경우의 수에 따른 감시 영역에 대한 방문 체크 => DFS
    # 케이스 별로 dfs 도중 total 사각지대가 현재 사각지대보다 작다면 백트래킹
