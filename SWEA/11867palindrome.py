T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    text = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1): # i, j는 회문 비교의 시작점
            flag = 1
            for k in range(M//2):
                if text[i][j+k] != text[i][j+(M-1)-k]:  # j는 M-1부터 (회문의 길이 // 2)만큼 안쪽까지 탐색  (왼<-오)
                    flag = 0
                    break

            if flag:
                print(f'#{tc}', end=' ')
                for k in range(M):
                    print(text[i][j+k], end='')
                print()

    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if text[j+k][i] != text[j+(M-1)-k][i]:
                    flag = 0
                    break

            if flag:
                print(f'#{tc}', end=' ')
                for k in range(M):
                    print(text[j+k][i], end='')
                print()

# 중복되는 코드 많은데 어떻게 합칠 수 없을까요?
# 합칠 수는 있는데 이 케이스는 따로 하는 게 더 나을지도.. (괜히 실수 안하기엔 이게 안전..)
# 만약 합치면 각 좌표마다 가로 한번 세로 한번 탐색하면서 나아가는 방식으로~!

# 슬라이싱 쓸거면 ?
#   => 슬라이싱은 가로방향만 가능!!
#      => 전치행렬 생성해서 세로방향 판별~!
