N = int(input())
arr = [input() for _ in range(N)]
arr = list(set(arr))
N = len(arr)

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if len(arr[j]) > len(arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

for j in range(N-1):
    if len(arr[j]) == len(arr[j + 1]):
        for k in range(len(arr[j])):
            if arr[j][k] == arr[j+1][k]:
                continue
            if arr[j][k] > arr[j+1][k]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                break

print(arr)
# for word in arr:
#     print(word)
