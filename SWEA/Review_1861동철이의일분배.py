# def perm(n, k, curmax):
#     global ans
#
#     if ans >= curmax:      # =부호 꼭 넣어줘야 함!!
#         return
#
#     if n == k:
#         ans = max(ans, curmax)
#         return
#
#     else:
#         for i in range(n):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 P[k] = A[i]
#                 perm(n, k + 1, curmax * (arr[k][P[k]] * 0.01))     # arr[k][P[k]] == arr[k][i]
#                 visited[i] = 0
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     visited = [0] * N
#     A = list(range(N))
#     P = [0] * N
#
#     ans = 0
#     perm(N, 0, 1)    # 확률이므로 시작 값은 1
#
#     print(f'#{tc} {ans * 100:.6f}')
#

# 형식 지정자
# 16진수를 10진수로 입력받기
num = int(input(), 16)

# 10진수로 출력
print(num)

# 16진수로 출력
print(f'{num:x}')      # ff - 16진수 소문자 : x는 hexa를 의미
print(f'{num:+x}')     # +ff - 원래 부호는 음수일 때만 나오는데 +해주면 항상 부호 출력
print(f'{num:X}')      # FF - 16진수 대문자
print(f'{num:b}')      # 11111111 - 16진수 이진수
print(f'{num:<16b}')   # 11111111 - 16진수 이진수 (좌측 정렬)
print(f'{num:>16b}')   #         11111111 - 16진수 이진수 (우측 정렬)
print(f'{num:^16b}')   #     11111111 - 16진수 이진수 (가운데 정렬)
