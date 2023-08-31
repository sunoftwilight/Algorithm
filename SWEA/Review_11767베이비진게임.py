def baby_gin(cnt):
    for i in range(10):             # triplet
        if cnt[i] >= 3:
            return True

    for i in range(8):              # run
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            return True


def game():
    cnt1 = [0] * 10
    cnt2 = [0] * 10

    for i in range(12):
        if i % 2 == 0:
            cnt1[arr[i]] += 1       # 카드 숫자별로 몇장 가지고 있는지 카운팅

        else:
            cnt2[arr[i]] += 1

        # 3장 이후부터
        if i > 4:
            if i % 2 == 0:
                if baby_gin(cnt1):
                    return 1

            else:
                if baby_gin(cnt2):
                    return 2

    return 0


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))      # 12장의 카드
    print(f'#{tc} {game()}')
