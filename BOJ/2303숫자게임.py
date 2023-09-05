def comb(n, r):
    global max_sum
    global max_who

    if r == 0:
        digit = sum(T) % 10
        # max_sum = max(digit, max_sum)
        if max_sum <= digit:
            max_sum = digit
            max_who = i
        return

    elif n < r:
        return

    else:
        T[r-1] = card[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


N = int(input())
max_who = 0
max_sum = 0

for i in range(1, N+1):
    card = list(map(int, input().split()))
    T = [0] * 3
    comb(5, 3)

print(max_who)