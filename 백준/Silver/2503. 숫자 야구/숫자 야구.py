N = int(input())
questions = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue

            num = str(i) + str(j) + str(k)
            is_correct = True

            for q, s, b in questions:
                q = str(q)
                strk, ball = 0, 0

                if num[0] == q[0]:
                    strk += 1
                elif q[0] in num:
                    ball += 1

                if num[1] == q[1]:
                    strk += 1
                elif q[1] in num:
                    ball += 1

                if num[2] == q[2]:
                    strk += 1
                elif q[2] in num:
                    ball += 1

                if s != strk or b != ball:
                    is_correct = False
                    break

            if is_correct:
                answer += 1

print(answer)
