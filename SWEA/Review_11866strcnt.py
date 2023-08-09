# 딕셔너리로 풀기
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    my_dic = {}

    # 중복 제거 및 0으로 초기화
    for key in str1:
        my_dic[key] = 0

    # 카운팅
    for key in str2:
        if key in my_dic:
        # if my_dic.get(key) != None: 위의 get 방식과 동일
            my_dic[key] += 1

    # 최대값 찾기
    ans = 0

    for c in my_dic.values():
        if ans < c:
            ans = c

    print(f'#{tc} {ans}')

