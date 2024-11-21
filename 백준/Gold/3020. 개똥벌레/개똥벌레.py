N, H = map(int, input().split())
cave = [0] * H

for k in range(N):
    j = int(input())
    if k % 2 == 0:
        cave[0] += 1
        if j < H:
            cave[j] -= 1
    else:
        cave[H-j] += 1

prefix = [0] * H
prefix[0] = cave[0]

for i in range(1, H):
    prefix[i] = prefix[i-1] + cave[i]

min_v = min(prefix)
counting = prefix.count(min_v)

print(min_v, counting)
