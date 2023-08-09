# N = int(input())
# arr = [input() for _ in range(N)]
#
# arr = list(set(arr))
# N = len(arr)
#
# arr.sort()
#
# for i in range(N-1, 0, -1):
#     for j in range(0, i):
#         if len(arr[j]) > len(arr[j+1]):
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#
# for word in arr:
#     print(word)

arr = ['b', 'c', 'A', 'a', 'C', 'B']
arr.sort()
print(arr)