def dfs(a):
    global cnt
    global flag

    if flag:
        return
	# 방문 체크 및 하고 싶은 일 (cnt 세기)
    visited[a] = 1
    cnt += 1

	# 최종 정점을 찾았다면 탐색 종료 및 flag 전환
    if a == B:
        flag = 1
        return

	# 아니라면 탐색 계속 이어나감
    for w in range(1, N+1):
        if adj[a][w] == 1 and visited[w] == 0:
            dfs(w)


N = int(input())
A, B = map(int, input().split())
M = int(input())

# 인접 리스트 및 방문 리스트 초기화
adj = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

# 연결된 정점 표시
for _ in range(M):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1

cnt = 0
flag = 0
dfs(A)

if flag != 0:
    flag = cnt
    
print(flag-1)