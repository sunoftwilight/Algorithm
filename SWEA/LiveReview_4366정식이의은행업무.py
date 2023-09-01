'''
1010 XOR 1000 => 0010
1010 XOR 0100 => 1110
1010 XOR 0010 => 1000
1010 XOR 0001 => 1011

XOR (바꾸고싶은 자리만 1인 2진수) => 한 자리만 변환됨!! (by bit연산)
'''

'''
(0 + 1) % 3 -> 1
(0 + 2) % 3 -> 2
(1 + 1) % 3 -> 2
(1 + 2) % 3 -> 0
(2 + 1) % 3 -> 0
(2 + 2) % 3 -> 1
'''

T = int(input())

for tc in range(1, T+1):
    A = input()              # 2진수
    B = list(map(int, input()))        # 3진수

    N = len(A)               # N자리 수 2진수
    M = len(B)               # M자리 수 3진수

    binary = int(A, 2)       # 정수로 변환
    bin_list = [0] * N       # 각 비트를 반전시킨 수 N개 저장

    ans = 0

    for i in range(N):       # 각 비트를 반전시킨 2진수 만들기
        bin_list[i] = binary ^ (1 << i)      # 비트 반전시킨 2진수가 10진수 형태로 저장됨

    for i in range(M):       # 3진수의 B[i] 자리를 바꾼 숫자 만들기
        num1 = 0             # (B[i] + 1) % 3
        num2 = 0             # (B[i] + 2) % 3

        for j in range(M):
            if i != j:       # 바꿀 자리가 아니라면
                num1 = num1 * 3 + B[j]
                num2 = num2 * 3 + B[j]

            else:
                num1 = num1 * 3 + (B[j] + 1) % 3
                num2 = num2 * 3 + (B[j] + 2) % 3

        if num1 in bin_list:
            ans = num1
            break

        if num2 in bin_list:
            ans = num2
            break

    print(f'#{tc} {ans}')
