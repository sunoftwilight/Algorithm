def perm(arr, k):
    if k >= M:                   # 목표한 k개의 원소 모두 선택 시
        print(*arr)              # 결과 출력 및 재귀 종료
        return

    for j in range(N):
        perm(arr + [nums[j]], k + 1)   # k+1번째 원소 선택


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for i in range(N):
    perm([nums[i]], 1)     # 수열 첫 원소 선택
