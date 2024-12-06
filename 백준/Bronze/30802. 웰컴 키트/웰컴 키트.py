N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

P_quo, P_rem = divmod(N, P)
P_cnt = [P_quo, P_rem]

T_cnt = 0
for n in sizes:
    T_quo, T_rem = divmod(n, T)

    T_cnt += T_quo

    if T_rem:
        T_cnt += 1

print(T_cnt)
print(*P_cnt)