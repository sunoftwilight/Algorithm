# 그냥 pop은 시간초과 발생 -> deque 써보자
from collections import deque
# deque보다 더 빠른 방법은 없나? -> index 접근!!

def merge(left, right):
    result = []

    # 두 리스트 중에 하나가 남으면
    while left or right:
        # 둘 다 남았을 때
        if left and right:
            if left[0] < right[0]:
                # result.append(left.pop(0))
                result.append(left.popleft())

            else:
                # result.append(right.pop(0))
                result.append(right.popleft())

        # # 왼쪽만 남았을 때
        # elif left:
        #     # result.append(left.pop(0))
        #     result.append(left.popleft())
        #
        # # 오른쪽만 남았을 때
        # elif right:
        #     # result.append(right.pop(0))
        #     result.append(right.popleft())

    # 왼쪽만 남았을 때
    if left:
        # extend
        result += left
    # 오른쪽만 남았을 때
    if right:
        result.extend(right)

    return result


def merge_sort(a):
    global cnt

    # basis
    if len(a) == 1:
        return a

    # 배열을 절반으로 나누어 각각 별도의 정렬 진행
    else:
        mid = len(a) // 2
        # left = a[:mid]
        # right = a[mid:]
        # left = merge_sort(left)
        # right = merge_sort(right)

        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])

        if left[-1] > right[-1]:
            cnt += 1

        return merge(left, right)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    # 비파괴 정렬
    arr = merge_sort(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')
