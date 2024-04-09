def bfs(visited, n, graph):
    Q = [1]
    visited[1] = 1

    while Q:
        c = Q.pop(0)

        for i in graph[c]:
            if visited[i] == 0:
                Q.append(i)
                visited[i] += visited[c] + 1


def solution(n, edge):
    answer = 0
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)

    visited = [0] * (n + 1)
    bfs(visited, n, graph)
    
    max_len = max(visited)
    answer = visited.count(max_len)

    return answer