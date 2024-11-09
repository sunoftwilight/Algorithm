X, Y, W, H = map(int, input().split())
answer = min(W-X, X, H-Y, Y)

print(answer)
