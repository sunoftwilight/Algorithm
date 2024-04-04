def perm(user_id, banned_id, n, k):
    global p, visited, answer

    if k >= n:
        tmp = [False] * len(banned_id)

        for idx in range(len(banned_id)):
            if len(p[idx]) == len(banned_id[idx]):
                tmp_txt = list(p[idx])
                for k in range(len(p[idx])):
                    if banned_id[idx][k] == '*' and tmp_txt[k] != banned_id[idx][k]:
                        tmp_txt[k] = '*'

                if tmp_txt == list(banned_id[idx]):
                    tmp[idx] = True

                else:
                    return

        if tmp.count(True) == len(banned_id):
            case = sorted(p)
            if case not in answer:
                answer.append(case)

        return

    else:
        for i in range(len(user_id)):
            if visited[i] == False:
                visited[i] = True
                p[k] = user_id[i]
                perm(user_id, banned_id, n, k + 1)
                visited[i] = False


def solution(user_id, banned_id):
    global p, visited, answer

    answer = []

    p = [False] * len(banned_id)
    visited = [False] * len(user_id)

    perm(user_id, banned_id, len(banned_id), 0)

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

print(solution(user_id, banned_id))