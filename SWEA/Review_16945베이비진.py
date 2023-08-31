def baby_gin():
    global ans

    check = 0

    # triplet 확인
    if p[0] == p[1] and p[1] == p[2]: check += 1
    if p[3] == p[4] and p[4] == p[5]: check += 1

    # run 확인
    if p[0] + 1 == p[1] and p[1] + 1 == p[2]: check += 1
    if p[3] + 1 == p[4] and p[4] + 1 == p[5]: check += 1

    # baby gin 확인
    if check == 2:
        ans = 1
        return


def perm(n, k):
    if n == k:
        baby_gin()

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = arr[i]
                perm(n, k + 1)
                visited[i] = 0


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input()))

    N = len(arr)
    p = [0] * N
    visited = [0] * N

    ans = 0
    perm(N, 0)

    print(f'#{tc} {ans}')
