T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0

    for i in range(1 << N):  # 1 << n : 부분 집합의 개수
        total = 0
        for j in range(N):  # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i의 j번 비트가 1인 경우
                total += A[j]

        if total == K:
            cnt += 1

    print(f'#{tc} {cnt}')
