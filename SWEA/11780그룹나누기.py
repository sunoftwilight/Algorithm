def solve(v):
    global cnt

    Q = [v]
    visited[v] = 1

    while Q:
        v = Q.pop(0)

        # 하고 싶은 일
        for w in adj_list[v]:
            if visited[w] == 0:       # if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1

    cnt += 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    adj_list = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    # 인접 리스트 만들기
    for i in range(M):
        s, e = arr[2 * i], arr[2 * i + 1]
        adj_list[s].append(e)
        adj_list[e].append(s)

    cnt = 0
    for j in range(1, N+1):
        if visited[j] == 0:
            solve(j)

    print(f'#{tc} {cnt}')