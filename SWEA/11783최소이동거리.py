'''
Dijkstra Algorithm

- 인접 행렬
- 가중치 배열
- 방문 리스트

1. 시작점 설정
2. 정점 갯수만큼 반복
    2-1. 최소값
    2-2. 방문체크
    2-3. 가중치 갱신
'''


def dijkstra(s):
    # 1. 시작점 설정
    D[s] = 0

    # 2. 정점 개수만큼 반복
    for i in range(N+1):

        # 2-1. 최소값 확인
        min_v = 987654321
        for j in range(N+1):
            if visited[j] == 0 and D[j] < min_v:
                min_v = D[j]
                v = j

        # 2-2. 방문 체크
        visited[v] = 1

        # 여기서 하고 싶은 일 체크해서 정답 리턴
        # if v == N:
        #     return D[v]

        # 2-3. 가중치 갱신
        for k in range(N+1):
            if visited[k] == 0 and adj[v][k]:
                if D[k] > D[v] + adj[v][k]:
                    D[k] = D[v] + adj[v][k]


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)

    D = [987654321] * (N+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    dijkstra(0)
    print(f'#{tc} {D[N]}')