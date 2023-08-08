T = int(input())

for tc in range(1, T+1):
    text = input()
    N = len(text)

    chk = 0
    ans = 1                         # 처음엔 회문이라 가정하고

    for i in range(N // 2):
        if text[i] != text[N-1-i]:  # 하나라도 틀린게 나오면 회문이 아니니까
            ans = 0                 # 0으로 바꾸고
            break                   # 이미 회문 아님을 판별했으니 뒤는 검사할 필요 X

    print(f'#{tc} {ans}')
