def rtt(wheel, di):
    if di == 1:                          # 시계 방향 회전
        return [wheel[-1]] + wheel[:7]

    elif di == -1:                       # 반시계 방향 회전
        return wheel[1:] + [wheel[0]]


def rotate_wheel(n, d, touch):
    global wheels

    wheels[n] = rtt(wheels[n], d)

    is_odd = True if n % 2 else False    # n과 같은 방향인가
    rot = d
    rvs = -1 if d == 1 else 1

    # 좌측 바퀴
    idx = n - 1
    while idx >= 0:
        if touch[idx]:
            if idx % 2 == is_odd:
                wheels[idx] = rtt(wheels[idx], rot)

            else:
                wheels[idx] = rtt(wheels[idx], rvs)

            idx -= 1

        else:
            break

    # n번 바퀴 + 우측 바퀴
    idx = n
    while idx < 3:
        if touch[idx]:
            if (idx + 1) % 2 == is_odd:
                wheels[idx + 1] = rtt(wheels[idx + 1], rot)

            else:
                wheels[idx + 1] = rtt(wheels[idx + 1], rvs)

            idx += 1

        else:
            break


wheels = [list(input()) for _ in range(4)]
K = int(input())
rotation_cmd = [list(map(int, input().split())) for _ in range(K)]

score = 0

for num, direct in rotation_cmd:
    touched = [False] * 3

    # 맞닿은 부분 극성 확인
    for i in range(3):
        if wheels[i][2] != wheels[i+1][6]:
            touched[i] = True

    # 바퀴 회전
    rotate_wheel(num-1, direct, touched)

# 점수 계산
for i in range(4):
    if wheels[i][0] == '1':
        score += 2 ** i

print(score)