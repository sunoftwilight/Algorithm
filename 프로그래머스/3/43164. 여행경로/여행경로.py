def solution(tickets):
    global n

    answer = []
    n = len(tickets)

    se = {}

    for ticket in tickets:
        if se.get(ticket[0]):
            se[ticket[0]].append([ticket[1], 0])
        else:
            se[ticket[0]] = [[ticket[1], 0]]

    def dfs(start, channel, depth):
        global n

        if depth == n:
            answer.append(channel)
            return

        if se.get(start):
            for i in range(len(se[start])):
                if not se[start][i][1]:
                    se[start][i][1] = 1
                    dfs(se[start][i][0], channel + [se[start][i][0]], depth + 1)
                    se[start][i][1] = 0

    dfs('ICN', ['ICN'], 0)
    answer.sort()

    return answer[0]