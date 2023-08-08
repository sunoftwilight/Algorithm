# 브루트포스 알고리즘 정도는 직접 구현할 수 있어야한다...ㅠㅠ
def brute_force(p, t):
    N, M = len(t), len(p)

    for i in range(N-M+1):
        flag = 1
        for j in range(M):
            if t[i+j] != p[j]:
                flag = 0
                break
        if flag:
            return 1         # return i를 사용하면 find 함수와 동일한 기능

    return -1


T = int(input())

for tc in range(1, T+1):
    pattern = input()
    text = input()

    print(f'#{tc} {brute_force(pattern, text)}')
