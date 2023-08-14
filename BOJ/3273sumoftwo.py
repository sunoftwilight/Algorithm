N = int(input())
a = list(map(int, input().split()))
X = int(input())

S2 = []

for i in range(1 << N):
    s = []
    for j in range(N):
        if i & (1 << j):
            s.append(a[j])
            if len(s) > 2:
                break
    if len(s) == 2:
        S2.append(s)

cnt = 0

for i in range(len(S2)):
    if sum(S2[i]) == X:
        cnt += 1

print(cnt)

a.sort()

s = cnt = 0
e = len(a) - 1

while s < e:
# 처음 코드 : while s <= e <= len(a) - 1
# s = e인 경우도 while 실행 조건으로 줌 근데 막상 s = e인데 a[s] + a[e] == X인 조건에서의 실행은 안줌
# 그래서 얘가 s = e면서 a[s]+a[e]==X일 때는 인덱스 조정 없이 계속 s = e인 상태로
# 아무 일도 못하면서 while안에 갇히게 되는거임 ㅠㅠ
    if a[s] + a[e] < X:
        s += 1

    elif a[s] + a[e] > X:
        e -= 1

    elif a[s] + a[e] == X:
        cnt += 1
        s += 1
        # 이건 생각도 몬함 (왜 넣냐? 이거는 어차피 중복되는 수가 리스트에 없음
        # => 그러면 같아진 순간에서 s나 e 하나만 옮겨서는 죽어도 목표값에 도달 못함)
        e -= 1

print(cnt)
