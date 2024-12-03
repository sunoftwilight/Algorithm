H, M = map(int, input().split())

if M >= 45:
    M -= 45
    print(H, M)

else:
    if not H:
        H = 23
    else:
        H -= 1

    M += 15
    print(H, M)