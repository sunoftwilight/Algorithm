"""
카운팅 배열은 수 번호의 방? 홀수 번호의 방? => 복도를 기준으로!

복도 번호
   -> 짝수 // 2
   -> (홀수 + 1) // 2
=> 복도 번호 = (방 번호 + 방번호 % 2) // 2

"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 학생 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 201     # 방 사이 공간을 지나는 사람 수

    # arr의 각 요소가 list이고, 해당 list는 2개의 요소 -> 해당 요소들을 꺼내겠다!
    for a, b in arr:
        a = (a + a % 2) // 2
        b = (b + b % 2) // 2
        for i in range(min(a, b), max(a, b)+1):    # a <= b 라는 보장 X  => 대소 비교해서 작은 출발 -> 큰 도착
            cnt[i] += 1

    print(f'#{tc} {max(cnt)}')
