N, K = map(int, input().split())

girl = [0] * 7
boy = [0] * 7
for _ in range(N):
    S, Y = map(int, input().split())

    if S:
        boy[Y] += 1
    else:
        girl[Y] += 1

cnt = 0
for i in range(1, 7):
    cnt += girl[i] // K
    if girl[i] % K != 0:
        cnt += 1

    cnt += boy[i] // K
    if boy[i] % K != 0:
        cnt += 1

print(cnt)