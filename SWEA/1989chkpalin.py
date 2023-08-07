T = int(input())

for tc in range(1, T+1):
    text = input()
    N = len(text)

    chk = 0
    ans = 1

    for i in range(N // 2):
        print(text[i], text[N-1-i])
        if text[i] != text[N-1-i]:
            ans = 0
            break

    print(f'#{tc} {ans}')
