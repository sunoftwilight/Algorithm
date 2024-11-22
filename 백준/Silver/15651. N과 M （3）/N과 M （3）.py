def perm(arr, k):
    if k >= M:                   # 목표한 k개의 원소 모두 선택 시
        print(*arr)              # 결과 출력 및 재귀 종료
        return

    for j in range(1, N+1):
        perm(arr + [j], k + 1)   # k+1번째 원소 선택


N, M = map(int, input().split())

for i in range(1, N+1):
    perm([i], 1)     # 수열 첫 원소 선택