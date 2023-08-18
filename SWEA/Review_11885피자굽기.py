'''
피자를 중간에 꺼내서 확인하고 다시 넣을 수 있다!
: deQ -> 확인 (= C // 2) -> enQ
- * - * - * - * - * - * - * - * - * - * - * - - * - * -

cheese = [7, 2, 6, 5, 3]
Q = [(1, 7), (2, 2), (3, 6) ...] 인덱스 함께 저장

pizza = Q.pop(0)     # 7
cheese[pizza //= 2   # 3

if cheese[pizza] != 0:   # 치즈 덜 녹았으면
    Q.append(pizza)      # 다시 넣기

elif idx <= M:           # 치즈 다 녹았으면
    Q.append(idx)        # 다음 피자 넣기
    idx += 1             # (idx는 cheese 리스트의 인덱스)
'''


def solve():
    Q = []

    # 화덕에 피자 넣기
    for i in range(1, N+1):
        Q.append(i)

    idx = N + 1    # 다음에 화덕에 들어갈 피자 번호

    while len(Q) > 1:
        # 피자를 꺼내서 치즈 확인
        pizza = Q.pop(0)
        cheese[pizza] //= 2    # 치즈 녹이기

        # 치즈가 남아 있으면
        if cheese[pizza] > 0:
            Q.append(pizza)
        # 치즈가 다 녹았으면
        elif idx <= M:         # else로 하면 안됨!! 피자 개수는 정해져있음
            Q.append(idx)
            idx += 1

    return Q[0]                # 마지막 남은 피자 return


T = int(input())

for tc in range(1, T+1):
    # 화덕 크기, 피자 수
    N, M = map(int, input().split())
    cheese = [0] + list(map(int, input().split()))    # cheese의 인덱스 1부터 시작할게~ (안헷갈리게)

    print(f'#{tc} {solve()}')
