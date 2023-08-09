T = int(input())

for tc in range(1, T+1):
    t, p = map(str, input().split())
    N = len(t)
    M = len(p)

    cnt = 0
    i = 0    # while문에서 사용될 변수 초기화

    while i < N - M + 1:
        flag = 1
        for j in range(M):
            if t[i + j] != p[j]:
                flag = 0
                break

        if flag:
            cnt += 1
            i += M - 1      # 패턴의 길이만큼 이동

        i += 1              # while문 종료 조건 달성을 위한 증감식

    typing = cnt + (N - M * cnt)
    print(f'#{tc} {typing}')
