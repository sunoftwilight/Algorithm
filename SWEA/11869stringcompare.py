T = int(input())

for tc in range(1, T+1):
    s1 = input()
    s2 = input()

    ans = 0
    for i in range(len(s2)):
        compare = 0
        if s2[i] == s1[0]:
            for j in range(len(s1)):
                if i + j < len(s2) and s2[i+j] == s1[j]:
                    compare += 1

            if compare == len(s1):
                ans = 1

    print(f'#{tc} {ans}')
