def dfs():
    pass

def find_graph(s):
    global graph, dounut, makdae, eight

    start_with = graph[s]
    flag = [False] * len(start_with)

    for i in range(len(start_with)):
        start_with[i]

    if flag == [False]:
        makdae += 1

    elif flag == [True]:
        dounut += 1

    elif flag == [True, True]:
        eight += 1

    else:
        makdae += 1
        dounut += 1

    return


def solution(edges):
    global graph, dounut, makdae, eight

    answer = [0] * 4
    dounut, makdae, eight = 0, 0, 0

    N_node = max(map(max, edges))
    graph = [[] for _ in range(N_node + 1)]

    for i, j in edges:
        graph[i].append(j)

    print(graph)

    center = 0
    for k in range(1, N_node + 1):
        if len(graph[center]) < len(graph[k]):
            center = k

    answer[0] = center

    for m in graph[center]:
        find_graph(m)


    return answer


print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
