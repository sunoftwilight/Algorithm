N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for i in range(N):
    is_slope = True
    is_down = True if arr[i][0] - arr[i][1] >= 0 else False

    installed = [False] * N

    j = 1
    while j < N:
        diff = arr[i][j - 1] - arr[i][j]

        if diff == 0:
            j += 1

        elif diff > 1 or diff < -1:
            is_slope = False
            break

        else:
            is_install = True

            for k in range(L):
                if diff == 1:
                    if not (0 <= j + k < N and not installed[j + k] and arr[i][j + k] == arr[i][j]):
                        is_install = False
                        break

                elif diff == -1:
                    if not (0 <= j - 1 - k < N and not installed[j - 1 - k]  and arr[i][j - 1 - k] == arr[i][j - 1]):
                        is_install = False
                        break

            if is_install:
                if diff == 1:
                    for k in range(L):
                        installed[j + k] = True
                    j += L

                elif diff == -1:
                    for k in range(L):
                        installed[j - 1 - k] = True
                    j += 1

            else:
                is_slope = False
                break

    if is_slope:
        answer += 1


for j in range(N):
    is_slope = True
    is_down = True if arr[0][j] - arr[1][j] >= 0 else False

    installed = [False] * N

    i = 1
    while i < N:
        diff = arr[i - 1][j] - arr[i][j]

        if diff == 0:
            i += 1

        elif diff > 1 or diff < -1:
            is_slope = False
            break

        else:
            is_install = True

            for k in range(L):
                if diff == 1:
                    if not (0 <= i + k < N and not installed[i + k] and arr[i + k][j] == arr[i][j]):
                        is_install = False
                        break

                elif diff == -1:
                    if not (0 <= i - 1 - k < N and not installed[i - 1 - k] and arr[i - 1 - k][j] == arr[i - 1][j]):
                        is_install = False
                        break

            if is_install:
                if diff == 1:
                    for k in range(L):
                        installed[i + k] = True
                    i += L

                elif diff == -1:
                    for k in range(L):
                        installed[i - 1 - k] = True
                    i += 1

            else:
                is_slope = False
                break

    if is_slope:
        answer += 1

print(answer)