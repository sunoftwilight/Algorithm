x, b = map(int, input().split())

answer = ''
minus = x < 0 and b >= 0

if minus:
    x *= (-1)

while x:
    quo, rmi = divmod(x, b)

    if rmi < 0:
        quo += 1
        rmi += (-1) * b

    answer += str(rmi)
    x = quo

if minus:
    answer += '-'

if answer:
    print(answer[::-1])
else:
    print(0)
