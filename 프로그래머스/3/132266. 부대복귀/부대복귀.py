from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    adjMatrix = [[] for _ in range(n + 1)]
    
    for i, j in roads:
        adjMatrix[i].append(j)
        adjMatrix[j].append(i)
        
    
    def bfs(s):
        Q = deque([s])
        
        cost = [-1] * (n + 1)
        cost[destination] = 0
        
        while Q:
            current = Q.popleft()
            
            for i in range(len(adjMatrix[current])):
                if cost[adjMatrix[current][i]] == -1:
                    cost[adjMatrix[current][i]] = cost[current] + 1
                    Q.append(adjMatrix[current][i])
                    
        return cost
    
    costs = bfs(destination)
    
    for source in sources:
        answer.append(costs[source])
        
    return answer