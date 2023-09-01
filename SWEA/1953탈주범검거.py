def manhole(r, c, l):
    global cnt

    l -= 1

    if l == 0 or arr[r][c] == 0 or visited[r][c]:
        if arr[r][c] != 0 and visited[r][c] == 0:
            cnt += 1
        return

    else:
        if visited[r][c] == 0:
            cnt += 1

        if arr[r][c] == 1:
            visited[r][c] += 1
            if c+1 < M and arr[r][c+1] in [1, 3, 6, 7]: manhole(r, c+1, l)
            if r+1 < N and arr[r+1][c] in [1, 2, 4, 7]: manhole(r+1, c, l)
            if 0 <= c-1 and arr[r][c-1] in [1, 3, 4, 5]: manhole(r, c-1, l)
            if 0 <= r-1 and arr[r-1][c] in [1, 2, 5, 6]: manhole(r-1, c, l)

        if arr[r][c] == 2:
            visited[r][c] += 1
            if 0 <= r-1 and arr[r-1][c] in [1, 2, 5, 6]: manhole(r-1, c, l)
            if r+1 < N and arr[r+1][c] in [1, 2, 4, 7]: manhole(r+1, c, l)

        if arr[r][c] == 3:
            visited[r][c] += 1
            if c+1 < M and arr[r][c+1] in [1, 3, 6, 7]: manhole(r, c+1, l)
            if 0 <= c-1 and arr[r][c-1] in [1, 3, 4, 5]: manhole(r, c-1, l)

        if arr[r][c] == 4:
            visited[r][c] += 1
            if c + 1 < M and arr[r][c+1] in [1, 3, 6, 7]: manhole(r, c+1, l)
            if 0 <= r - 1 and arr[r-1][c] in [1, 2, 5, 6]: manhole(r-1, c, l)

        if arr[r][c] == 5:
            visited[r][c] += 1
            if c+1 < M and arr[r][c+1] in [1, 3, 6, 7]: manhole(r, c+1, l)
            if r+1 < N and arr[r+1][c] in [1, 2, 4, 7]: manhole(r+1, c, l)

        if arr[r][c] == 6:
            visited[r][c] += 1
            if r+1 < N and arr[r+1][c] in [1, 2, 4, 7]: manhole(r+1, c, l)
            if 0 <= c-1 and arr[r][c-1] in [1, 3, 4, 5]: manhole(r, c-1, l)

        if arr[r][c] == 7:
            visited[r][c] += 1
            if 0 <= c-1 and arr[r][c-1] in [1, 3, 4, 5]: manhole(r, c-1, l)
            if 0 <= r-1 and arr[r-1][c] in [1, 2, 5, 6]: manhole(r-1, c, l)


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    cnt = 0
    manhole(R, C, L)

    print(f'#{tc} {cnt}')
