X, Y, W, S = map(int, input().split())

ans1 = (X + Y) * W

if (X + Y) % 2 == 0:
    ans2 = max(X, Y) * S
else:
    ans2 = (max(X, Y) - 1) * S + W

cnt = 0
ans3 = min(X, Y) * S + (max(X, Y)-min(X, Y)) * W

print(min(ans1, ans2, ans3))
