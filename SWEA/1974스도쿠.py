import sys; sys.stdin = open('1974_input.txt', 'r')

def chksdk():
    global flag
    # 행
    for i in range(N):
        for k in num:
            if k not in arr[i]:
                flag = 0
                return flag

    # 열
    for j in range(N):
        lst = []
        for i in range(N):
            lst.append(arr[i][j])

        for k in num:
            if k not in lst:
                flag = 0
                return flag

    # 3x3
    for i in range(0, N, 3):
        lst = []
        for j in range(0, N, 3):
            for m in range(3):
                for n in range(3):
                    lst.append(arr[i + m][j + n])
            for k in num:
                if k not in lst:
                    flag = 0
                    return flag


T = int(input())

for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    flag = 1
    chksdk()

    print(f'#{tc} {flag}')




