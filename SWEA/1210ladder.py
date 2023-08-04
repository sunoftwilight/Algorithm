T = 10

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]

    for idx in range(100):
        if arr[99][idx] == 2:
            idx2 = idx

    di = []
    dj = []

    for i in range(100):
        for j in range(100):
            pass
