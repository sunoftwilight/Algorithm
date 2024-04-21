def solution(n, s):

    if n > s:
        return [-1]

    quotient = s // n
    answer = [quotient] * n

    remainder = s % n

    if remainder:
        for i in range(n-1, -1, -1):
            if remainder:
                answer[i] += 1
                remainder -= 1

            else:
                break

    return answer