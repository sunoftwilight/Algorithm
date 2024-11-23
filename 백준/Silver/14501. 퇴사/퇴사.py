def counsel(day, pay):
    global max_pay

    if day == N:
        max_pay = max(max_pay, pay)
        return

    if day + task[day][0] <= N:
        counsel(day + task[day][0], pay + task[day][1])

    counsel(day + 1, pay)


N = int(input())
task = [list(map(int, input().split())) for _ in range(N)]
max_pay = 0

counsel(0, 0)

print(max_pay)
