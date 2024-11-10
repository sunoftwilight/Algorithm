N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

answer = 0

for a, b in zip(A, B):
    answer += a * b

print(answer)
