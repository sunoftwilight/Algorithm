word = input()
cnt = [-1] * 26

for i in range(len(word)):
    if cnt[ord(word[i]) - 97] == -1:
        cnt[ord(word[i]) - 97] = i

print(*cnt)