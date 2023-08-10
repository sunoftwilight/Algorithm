def dfs(v):
    global flag

    visited[v] = 1

    if v == B:         # 항상 하고 싶은 일은 여기에 선언해라!!! 밑에 탐색하다가 수행하지마!!!
        flag = 1
        return

    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)
            """
            원래 여기에 
            if w == B:
                return 1
        return 0 
            으로 코드 짰는데, 재귀에서는 return이 시작점으로 한번에 돌아가는 게 아니라 바로 직전 함수로 돌아가는거임
            그래서 return으로 1을 줬어도 바로 앞 함수로 돌아가면 다시 w==B 조건을 충족 못해서 return해준 1이 사라지게 됨
            따라서 재귀함수에서는 코드 중간에 return 하지 말고 flag를 사용하는 습관을 들이는 것이 좋음
            이번 문제의 경우에는 B를 방문 못했으면 visited[B] = 0,방문 했으면 visited[B] = 1로 변경될 것이므로 
            flag 사용 없이 dfs 모두 실행 후, visited[B]를 프린트 하면 결과를 잘 얻을 수 있다
            """


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    A, B = map(int, input().split())

    adj = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        s, e = temp[i][0], temp[i][1]
        adj[s][e] = 1

    flag = 0
    dfs(A)

    print(f'#{tc} {flag}')
