def dfs(k, pre):
    if k == N:
        return 1
    else:
        ans = 0
        for key in chk.keys():
            if pre == key:
                continue
            if chk[key] == 0:
                continue

            chk[key] -= 1
            ans += dfs(k + 1, key)
            chk[key] += 1
        return ans


txt = input()
N = len(txt)

chk = {}
for i in txt:
    if i in chk:
        chk[i] += 1
    else:
        chk[i] = 1

result = dfs(0, '')
print(result)