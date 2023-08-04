def binary_search(arr, n, key):
    s = 1
    e = n
    cnt = 0

    while s <= e:
        cnt += 1
        m = (s + e) // 2
        if key == arr[m]:
            return cnt
        elif key < arr[m]:
            e = m
        else:
            s = m
    return False


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    arr = [0] + list(range(1, P+1))
    a_cnt = binary_search(arr, P, A)
    b_cnt = binary_search(arr, P, B)

    if a_cnt > b_cnt:
        ans = 'B'
    elif a_cnt < b_cnt:
        ans = 'A'
    else:
        ans = '0'

    print(f'#{tc} {ans}')