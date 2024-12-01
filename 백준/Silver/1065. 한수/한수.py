N = int(input())
answer = 0

for n in range(1, N+1):
    num = str(n)

    is_han = True
    len_n = len(num)

    if len_n == 1:
        answer += 1
        continue

    idx = 1
    equal_minus = int(num[0]) - int(num[1])

    while idx < len_n - 1:
        if int(num[idx]) - int(num[idx + 1]) == equal_minus:
            idx += 1

        else:
            is_han = False
            break

    if is_han:
        answer += 1

print(answer)