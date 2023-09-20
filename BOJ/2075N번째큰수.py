N = int(input())
arr = []

for i in range(N):
    print(arr)
    arr += list(map(int, input().split()))
    arr.sort()
    arr = arr[len(arr)-N:]

print(arr[0])
