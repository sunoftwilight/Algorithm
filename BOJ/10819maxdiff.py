N = int(input())
arr = list(map(int, input().split()))

arr.sort()
print(arr)
new = []

for i in range(N//2):
    new.insert(0, arr[i])
    new.insert(-1, arr[N-1-i])

print(new)

total = 0

for i in range(N-1):
    total += abs(new[i]-new[i+1])

if N % 2:
    total += new[N // 2 + 1]

print(total)