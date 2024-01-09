A, B = map(int, input().split())

cnt = 0
while A < B:
    if (B % 10) != 1:
        if B % 2 == 0:
            B //= 2
            cnt += 1
        else:
            break

    else:
        B //= 10
        cnt += 1

    if A == B:
        cnt += 1
        break

if A != B:
    cnt = -1

print(cnt)

# A, B = map(int, input().split())
#
# cnt = 0
# while A < B:
#     if str(B)[-1] != "1":
#         if B % 2 == 0:
#             B //= 2
#             cnt += 1
#         else:
#             break
#
#     elif str(B)[-1] == "1":
#         # B = int(str(B)[0:len(str(B))-1])
#         B //= 10
#         cnt += 1
#
#     if A == B:
#         break
#
# if A != B:
#     cnt = -1
# else:
#     cnt += 1
#
# print(cnt)