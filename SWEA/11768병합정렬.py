def merge(left, right):
    global cnt_r

    mg = []

    # merge할 때 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt += 1
    if left[-1] > right[-1]:
        cnt_r += 1

    i = j = 0
    # left 배열과 right 배열이 모두 빌 때까지 병합 반복
    while len(left) - 1 >= i or len(right) - 1 >= j:
        # 왼쪽 오른쪽 둘 다 원소가 있다면
        if len(left) - 1 >= i and len(right) - 1 >= j:
            # 각각의 최소값을 비교하여 더 작은 수를 append 하고 인덱스 올리기
            if left[i] >= right[j]:
                mg.append(right[j])
                j += 1
            else:
                mg.append(left[i])
                i += 1

        # 왼쪽만 원소가 남았다면
        elif len(left) - 1 >= i and len(right) - 1 < j:
            # 왼쪽 배열에서 최소값부터 넣어주고 인덱스 올리기
            mg.append(left[i])
            i += 1

        # 오른쪽만 원소가 남았다면
        else:
            # 오른쪽 배열에서 최소값부터 넣어주고 인덱스 올리기
            mg.append(right[j])
            j += 1

    # 최종 병합된 배열 반환
    return mg


def merge_sort(a):
    # 배열의 길이가 1이면 분할 끝났음
    if len(a) == 1:
        return a

    # 아니라면
    else:
        # 가운데 지점(=기준점) 설정
        mid = len(a) // 2
        # mid 기준으로 앞쪽은 left, 뒷쪽은 right
        left = a[:mid]
        right = a[mid:]

        # 각각의 left, right에 대해서도 원소가 1개가 될 때까지 재귀 반복
        left = merge_sort(left)
        right = merge_sort(right)

        # 분할 끝났으면 left right에 대해 병합하러 가자~
        return merge(left, right)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt_r = 0
    mg_arr = merge_sort(arr)

    print(f'#{tc} {mg_arr[N//2]} {cnt_r}')
