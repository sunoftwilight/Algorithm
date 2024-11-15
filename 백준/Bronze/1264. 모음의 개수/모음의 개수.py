while True:
    msg = input().lower()

    if msg == '#':
        break

    answer = 0
    answer += msg.count('a')
    answer += msg.count('e')
    answer += msg.count('i')
    answer += msg.count('o')
    answer += msg.count('u')

    print(answer)
