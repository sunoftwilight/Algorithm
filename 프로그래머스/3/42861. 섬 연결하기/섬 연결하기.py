def prim(s, adj, visited, D, PI, n):
    # 시작점 설정
    D[s] = 0
    total = 0

    # 정점의 갯수만큼 선택하기
    for i in range(n):
        # 가중치 최소값 찾기
        min_v = 987654321
        for j in range(n):
            if visited[j] == 0 and D[j] < min_v:
                min_v = D[j]
                v = j  # 가중치가 최소인 정점 선택

        # 방문 처리 (선택) + 하고싶은 일
        visited[v] = 1
        total += adj[PI[v]][v]

        # 인접 정점의 가중치 갱신
        for w in range(n):
            if adj[v][w] and not visited[w]:
                if D[w] > adj[v][w]:
                    D[w] = adj[v][w]
                    PI[w] = v

    return total


def solution(n, costs):
    adj = [[0] * n for _ in range(n)]
    visited = [0] * n
    D = [987654321] * n
    PI = list(range(n))

    for i, j, w in costs:
        adj[i][j] = adj[j][i] = w

    answer = prim(0, adj, visited, D, PI, n)

    return answer

# print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))