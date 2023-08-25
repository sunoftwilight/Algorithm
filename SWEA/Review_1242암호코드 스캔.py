code = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

hex_to_bin = {
    '0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0], '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0], '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1], 'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1],
}


def solve():
    ans = 0

    # 2진수로 2차원 배열 순회
    for i in range(N):      # 행
        j = M * 4 - 1       # 열의 마지막 인덱스

        while j > 0:
            if arr[i][j] == 1 and arr[i-1][j] == 0:
                pwd = []
                for _ in range(8):     # 암호를 8번 구하기
                    c2 = c3 = c4 = 0   # 카운트

                    while arr[i][j] == 1: c4 += 1; j -= 1    # 1일 때, 개수 세기
                    while arr[i][j] == 0: c3 += 1; j -= 1    # 0일 때, 개수 세기
                    while arr[i][j] == 1: c2 += 1; j -= 1    # 1일 때, 개수 세기
                    while arr[i][j] == 0: j -= 1             # 0일 때, 이동

                    min_v = min(c2, c3, c4)                  # 최소값 구해서 나누기
                    pwd.append(code[(c2 // min_v, c3 // min_v, c4 // min_v)])
                # 검증해서 누적하기 : 뒤에서부터 저장되므로 인덱스의 짝수, 홀수가 바뀜
                even = pwd[0] + pwd[2] + pwd[4] + pwd[6]     # 거꾸로 넣었으므로 even 맞음
                odd = pwd[1] + pwd[3] + pwd[5] + pwd[7]

                if (odd * 3 + even) % 10 == 0:
                    ans += even + odd

                j += 1
                # 같은 행에 암호 코드 블럭이 겹쳐 있다면, 다음 암호 블럭에 도착
                # j를 오른쪽으로 한 칸 이동해야 함 (아래에서 j가 감소되므로)

            j -= 1          # 증감
    return ans


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hex_to_bin[tmp[j]]

    print(f'#{tc} {solve()}')
