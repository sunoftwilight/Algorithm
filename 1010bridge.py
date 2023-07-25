import sys
sys.setrecursionlimit(10**7)

def fact(n):
    if n == 1 or n == 0 :
        return 1
    return n * fact(n-1)


T = int(input())

for test_case in range(1, T+1) :
    N, M = map(int, input().split())

    brdg = int(fact(M) / ((fact(N) * fact(M-N))))

    print(f'#{test_case} {brdg}')