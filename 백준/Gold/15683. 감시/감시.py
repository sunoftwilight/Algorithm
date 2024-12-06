import copy

cctv = {
    1: [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3: [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)]],
    4: [[(0, 1), (1, 0), (0, -1)], [(0, 1), (1, 0), (-1, 0)], [(0, 1), (0, -1), (-1, 0)], [(1, 0), (0, -1), (-1, 0)]],
    5: [[(0, 1), (1, 0), (0, -1), (-1, 0)]],
}


def observe(room, cam):
    global min_hide

    if cam >= len(locs):
        tmp_hide = 0

        for k in range(N):
            tmp_hide += room[k].count(0)

            if tmp_hide >= min_hide:
                return

        min_hide = min(min_hide, tmp_hide)
        return

    (i, j) = locs[cam]
    cam_dir = cctv[arr[i][j]]

    for dirs in cam_dir:
        tmp_room = copy.deepcopy(room)
        for di, dj in dirs:
            ci, cj = i, j

            while True:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < N and 0 <= nj < M and tmp_room[ni][nj] != 6:
                    if tmp_room[ni][nj] == 0:
                        tmp_room[ni][nj] = '#'
                    ci, cj = ni, nj

                else:
                    break

        observe(tmp_room, cam + 1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

locs = []

for i in range(N):
    for j in range(M):
        if arr[i][j] in [1, 2, 3, 4, 5]:
            locs.append((i, j))

min_hide = N * M

tmp = copy.deepcopy(arr)
observe(tmp, 0)

print(min_hide)
