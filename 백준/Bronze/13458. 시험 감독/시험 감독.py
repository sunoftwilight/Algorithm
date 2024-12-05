N = int(input())
rooms = list(map(int, input().split()))
see1, see2 = map(int, input().split())

answer = N

for i in range(N):
    remain = rooms[i] - see1

    if remain > 0:
        quo, rem = divmod(remain, see2)
        answer += quo

        if rem:
            answer += 1

print(answer)