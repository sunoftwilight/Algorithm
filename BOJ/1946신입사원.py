T = int(input())

for tc in range(T):
    N = int(input())

    sinip = []
    for _ in range(N):
        sr, mj = map(int, input().split())
        sinip.append((sr, mj))

    sinip.sort()

    cnt = 1
    # 서류 면접 제일 잘 본 신입의 면접 점수
    best = sinip[0][1]

    for i in range(1, N):
        # 서류 제일 잘 본 사람의 면접 점수보다 내 면접 점수가 낮으면(=등수가 크면) 뽑힐 수 없음 (둘 다 뒤쳐짐)
        # best보다 내 면접 등수가 작아야 뽑힘
        # 내 면접 등수가 더 작으면 제일 높은 점수 갱신 (서류는 이미 판단 완료 + 면접 점수 컷 점점 올라가는 중)
        if best > sinip[i][1]:
            best = sinip[i][1]
            cnt += 1

    print(cnt)
