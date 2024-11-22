from itertools import permutations

N, M = map(int, input().split())
visited = [False] * (N + 1)

for perm in permutations(list(range(1, N+1)), M):
    print(*list(perm))
