# 10*10 칸을 만들고 색깔을 칠해나가는 방식!!!
# 좌표 구하는 것 X +color값 해주며 색칠
# => red = 1, blue = 2 이므로 3 이상이 되면 cnt +1

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 색칠 횟수
    arr = [[0] * 10 for _ in range(10)]    # {[0] * 10} * 10 은 얕은 복사이므로 사용X

    # 색칠하기
    for _ in range(N):     # 좌상단 & 우하단 좌표, color 입력
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):        # 가로 좌표
            for j in range(c1, c2+1):    # 세로 좌표
                arr[i][j] += color       # 칠하는 색의 숫자만큼 누적

    # 겹쳐진 칸의 개수 counting (= 3인 칸 찾기)
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
