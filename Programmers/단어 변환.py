from collections import deque


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return answer

    def bfs(s, k):

        Q = deque([])

        Q.append((s, k))

        while Q:
            begin, depth = Q.popleft()

            if begin == target:
                return depth

            for txt in words:
                is_trans = 0

                for i in range(len(begin)):
                    if begin[i] != txt[i]:
                        is_trans += 1

                        if is_trans > 1:
                            break

                if is_trans == 1:
                    Q.append((txt, depth + 1))

    answer = bfs(begin, 0)

    return answer


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
