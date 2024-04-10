def implement(many, stones, k):
    consecutive_empty = 0
    for stone in stones:
        if stone < many:
            consecutive_empty += 1
        else:
            consecutive_empty = 0

        if consecutive_empty >= k:
            return False

    return True


def solution(stones, k):
    max_stone = max(stones)

    s = 1
    e = max_stone

    while s <= e:
        m = (s + e) // 2

        if not implement(m, stones, k):
            e = m - 1

        else:
            s = m + 1

    return s - 1


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([7, 2, 8, 7, 2, 5, 9], 3))
