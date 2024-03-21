import copy

N = int(input())
arr = []

for _ in range(N):
    arr.append(input())

arr = list(set(arr))
ans = copy.deepcopy(arr)

for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j:
            if len(arr[i]) <= len(arr[j]) and arr[i] == arr[j][:len(arr[i])]:
                ans.remove(arr[i])
                break

print(len(ans))
