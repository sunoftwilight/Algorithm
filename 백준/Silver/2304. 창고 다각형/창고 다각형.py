N = int(input())
pillar = [list(map(int, input().split())) for _ in range(N)]

pillar.sort()

highest = 0
tmp_h = 0
for i in range(N):
    if pillar[i][1] >= tmp_h:
        tmp_h = pillar[i][1]
        highest = i

answer = 0
left_max_height = 0
left_tmp = 0

for i in range(highest+1):
    L, H = pillar[i]
    if left_max_height <= H:
        answer += (L - left_tmp) * left_max_height
        left_max_height = H
        left_tmp = L

right_max_height = 0
right_tmp = 0

for i in range(N-1, highest-1, -1):
    L, H = pillar[i]
    if right_max_height <= H:
        answer += (right_tmp - L) * right_max_height
        right_max_height = H
        right_tmp = L

print(answer + pillar[highest][1])
