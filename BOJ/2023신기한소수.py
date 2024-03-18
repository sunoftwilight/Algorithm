def dfs(num, depth):
    if depth >= N:
        print(num)
        return

    for j in sosu:
        dfs(num + j, depth + 1)


N = int(input())
sosu = ['1', '2', '3', '5', '7']

for i in sosu:
    dfs(i, 1)
