def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return answer

    works.sort(reverse=True)

    max_v = works[0]
    idx = 0

    while n:
        if works[idx] == max_v:
            works[idx] -= 1
            idx += 1
            n -= 1

        else:
            max_v = works[0]
            idx = 0

    for work in works:
        answer += work ** 2

    return answer


print(solution(4, [4, 3, 3]))  # 12
print(solution(1, [2, 1, 2]))  # 6
print(solution(3, [1, 1]))     # 0
print(solution(9, [1, 1, 1]))  # 0
