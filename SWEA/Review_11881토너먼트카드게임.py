def win(r1, r2):
    if arr[r1] == arr[r2]: return r1

    else:
        if arr[r1] == 1 and arr[r2] == 2: return r2
        elif arr[r1] == 1 and arr[r2] == 3: return r1
        elif arr[r1] == 2 and arr[r2] == 1: return r1
        elif arr[r1] == 2 and arr[r2] == 3: return r2
        elif arr[r1] == 3 and arr[r2] == 1: return r2
        elif arr[r1] == 3 and arr[r2] == 2: return r1


def game(l, r):    # l, r은 범위
    if l == r:
        return l

    else:
        r1 = game(l, (l+r) // 2)           # 총 4개의 요소를 가진 배열이면, 0, 1번째
        r2 = game((l+r) // 2 + 1, r)       # 2, 3번째
        return win(r1, r2)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {game(0, N-1) + 1}')