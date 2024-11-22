def perm(arr, k):
    if k >= M:                   # 목표한 k개의 원소 모두 선택 시
        print(*arr)              # 결과 출력 및 재귀 종료
        return

    for j in range(arr[-1]+1, N+1):
        if not visited[j]:       # 원소로 선택된 적 없다면
            visited[j] = True    # 방문 체크
            perm(arr + [j], k + 1)   # k+1번째 원소 선택
            visited[j] = False   # 방문 원복


N, M = map(int, input().split())
visited = [False] * (N + 1)

for i in range(1, N+1-M+1):
    visited[i] = True       # 방문 체크
    perm([i], 1)     # 수열 첫 원소 선택
    visited[i] = False      # 방문 원복