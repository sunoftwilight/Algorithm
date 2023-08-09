def row_max(arr, N):
    M = N

    while M > 0:
        for i in range(N):
            for j in range(N - M + 1):  # i, j는 회문 비교의 시작점
                flag = 1
                for k in range(M // 2):
                    # j는 M-1부터 (회문의 길이 // 2)만큼 안쪽까지 탐색  (왼<-오)
                    if arr[i][j + k] != arr[i][j + (M - 1) - k]:
                        flag = 0
                        break

                if flag:
                    return M    # 큰 거부터 탐색했으니까 회문 나오면 바로 return
        M -= 1  # 회문 아니면 회문 길이인 M 줄여서 다시 탐색


def col_max(arr, N):
    M = N

    while M > 0:
        for i in range(N):
            for j in range(N - M + 1):  # i, j는 회문 비교의 시작점
                flag = 1
                for k in range(M // 2):
                    # j는 M-1부터 (회문의 길이 // 2)만큼 안쪽까지 탐색  (왼<-오)
                    if arr[j + k][i] != arr[j + (M - 1) - k][i]:
                        flag = 0
                        break

                if flag:
                    return M    # 큰 거부터 탐색했으니까 회문 나오면 그게 제일 긴 길이이므로 바로 return
        M -= 1  # 회문 아니면 회문 길이인 M 줄여서 다시 탐색


T = 10
N = 100

for tc in range(1, T+1):
    no = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    r_max = row_max(arr, N)
    c_max = col_max(arr, N)

    ans = 0

    if r_max > c_max:
        ans = r_max
    else:
        ans = c_max

    print(f'#{tc} {ans}')

# 최대 회문 길이는 100이므로 회문의 길이가 긴 것부터 탐색을 시작하면
# 탐색을 위한 반복 횟수를 줄일 수 있음

