T = int(input())

for tc in range(T):
    J, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    candy_box = []    # 박스마다 넣을 수 있는 사탕의 개수를 담을 리스트

    for i in range(N):
        candy_box.append(box[i][0] * box[i][1])  # 사탕 개수 계산하여 담기

    candy_box.sort()  # 크기순으로 정렬

    box_cnt = max_cnt = 0  # 필요한 박스 개수, 선택한 박스에 대한 담을 수 있는 사탕 개수의 합
    idx = -1  # 뒤에서부터 탐색

    while max_cnt < J:     # 담을 사탕보다 상자에 넣을 수 있는 사탕 수가 적으면 박스 추가
        max_cnt += candy_box[idx]
        box_cnt += 1
        idx -= 1

    print(box_cnt)