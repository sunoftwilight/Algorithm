import sys

N, M = map(int, input().split())
pws = dict()

for _ in range(N):
    address, pw = sys.stdin.readline().strip().split()
    pws[address] = pw

for _ in range(M):
    find = sys.stdin.readline().strip()
    print(pws[find])