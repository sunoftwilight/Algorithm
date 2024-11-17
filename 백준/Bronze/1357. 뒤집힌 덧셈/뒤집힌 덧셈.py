X, Y = input().split()

X = int(X[::-1])
Y = int(Y[::-1])

new = X + Y
new = int(str(new)[::-1])

print(new)
