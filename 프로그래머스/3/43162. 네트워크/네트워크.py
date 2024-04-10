def dfs(i, n, computers):
    global visited

    visited[i] = 1

    for j in range(n):
        if computers[i][j] == 1 and visited[j] == 0:
            dfs(j, n, computers)


def solution(n, computers):
    global visited
    
    answer = 0
    visited = [0] * n

    for i in range(n):
        if visited[i] == 0:
            dfs(i, n, computers)
            answer += 1

    return answer
