def hoare_partition(a, l, r):
    # pivot = 배열의 가장 왼쪽 값으로 설정
    p = a[l]

    # 인덱스 초기화
    i, j = l, r

    # i가 j보다 작거나 같은 경우
    while i <= j:

        # 왼쪽에서부터 pivot보다 큰 값을 찾을 때까지 오른쪽으로 (i += 1)
        while i <= j and a[i] <= p:
            i += 1

        # 오른쪽에서부터 pivot보다 작은 값을 찾을 때까지 왼쪽으로 (j -= 1)
        while i <= j and a[j] >= p:
            j -= 1

        # pivot보다 큰 i와 pivot보다 작은 j를 찾았다면, i <-> j swap
        if i < j: a[i], a[j] = a[j], a[i]

    # 이후 i > j가 되어 두 인덱스가 교차되었다면 pivot과 j의 값을 교환하여 pivot의 자리를 찾아줌
    a[l], a[j] = a[j], a[l]

    return j    # pivot의 자리


def quick_sort(a, l, r):
    # sort가 완료된 후에는 재귀를 빠져나올 수 있도록 l < r 만족할 때만 함수 실행 (l, r의 교차 방지)
    if l < r:
        # pivot = 기준점
        pivot = hoare_partition(a, l, r)

        # pivot 제외하고 왼쪽 애들끼리 Quick sort
        quick_sort(a, l, pivot - 1)

        # pivot 제외하고 오른쪽 애들끼리 Quick sort
        quick_sort(a, pivot + 1, r)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr)-1)

    print(f'#{tc} {arr[N//2]}')
