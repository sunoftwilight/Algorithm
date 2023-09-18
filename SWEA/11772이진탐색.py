def binary_search(target):
    global cnt

    # 정렬된 배열의 범위 중 제일 작은 수의 idx = low
    low = 0
    # 정렬된 배열의 범위 중 제일 큰 수의 idx = high
    high = len(N_arr) - 1

    # 양쪽 구간 번갈아 선택 하는지 확인할 flag
    # 가장 첫번째 탐색 : flag = -1
    # 직전에 왼쪽 다녀옴 : flag = 0
    # 직전에 오른쪽 다녀옴 : flag = 1
    flag = -1

    # low가 high를 넘지 않는 선에서(교차되지 않는 선에서) 탐색 진행
    while low <= high:
        # mid의 idx는 low와 high의 가운데
        mid = (low + high) // 2

        # mid의 값이 찾으려는 값보다 크면
        if N_arr[mid] > target:
            # high를 mid의 바로 왼쪽으로 변경하여 mid 미만 구간만 탐색
            high = mid - 1

            # 만약 처음으로 탐색 시작한 곳(flag=-1)이 왼쪽이거나,
            # 오른쪽에 갔다가(flag=1) 왼쪽에 온 거라면
            if flag == -1 or flag == 1:
                # flag = 0으로 변경함으로써 왼쪽 방문 표시
                flag = 0

            # 만약 왼쪽을 연속적으로 방문한거라면(flag=0) 탐색 종료
            else:
                return

        # mid의 값이 찾으려는 값보다 작으면
        elif N_arr[mid] < target:
            # low를 mid의 바로 오른쪽으로 변경하여 mid 초과 구간만 탐색
            low = mid + 1

            # 만약 처음으로 탐색 시작한 곳(flag=-1)이 오른쪽이거나,
            # 왼쪽에 갔다가(flag=0) 오른쪽에 온 거라면
            if flag == -1 or flag == 0:
                # flag = 1으로 변경함으로써 왼쪽 방문 표시
                flag = 1

            # 만약 오른쪽을 연속적으로 방문한거라면(flag=1) 탐색 종료
            else:
                return

        # 위의 판별을 반복하다가 mid의 값이 찾으려는 값과 같아지면
        else:
            # 비로소 cnt를 +1하고 탐색 종료
            cnt += 1
            return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_arr = list(map(int, input().split()))
    M_arr = list(map(int, input().split()))

    # 이진 탐색을 위한 기본 세팅 (정렬)
    N_arr.sort()

    cnt = 0

    for i in range(M):
        binary_search(M_arr[i])

    print(f'#{tc} {cnt}')
