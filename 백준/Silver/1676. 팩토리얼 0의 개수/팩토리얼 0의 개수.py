N = int(input())

num = 1
for i in range(1, N+1):
    num *= i

num = str(num)

ans = 0
for i in range(len(num)-1, -1, -1):
    if num[i] != '0':
        break

    ans += 1

print(ans)