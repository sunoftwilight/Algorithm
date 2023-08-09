def my_find(t, p):
    global ans    # ans를 global로 선언하여 return 없이도 사용 가능 (재귀 등 return을 계속해야할 때 사용하면 좋음)

    for i in range(len(t)-len(p)+1):   # text
        flag = 1

        for j in range(len(p)):        # pattern
            if t[i + j] != p[j]:
                flag = 0
                break

        if flag:
            ans += 1


T = 10

for tc in range(1, T+1):
    case = int(input())

    pattern = input()
    text = input()

    ans = 0

    print(f'#{case} {ans}')

# # 단비언니 코드 (by split)
# T = 10
# for _ in range(T):
#     tc = int(input())
#     target = input()
#     string = input()
#
#     a = string.split(target)
#     print(a)
#     print(f"#{tc} {len(a) - 1}")

