import sys
sys.stdin = open('GNS_test_input.txt', 'r')
sys.stdout = open('GNS_output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    temp = input()   # dummy
    arr = list(map(str, input().split()))
    N = len(arr)

    num = {
        "ZRO" : 0,
        "ONE" : 1,
        "TWO" : 2,
        "THR" : 3,
        "FOR" : 4,
        "FIV" : 5,
        "SIX" : 6,
        "SVN" : 7,
        "EGT" : 8,
        "NIN" : 9,
    }

    for i in range(N):
        arr[i] = num[arr[i]]

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    txtnum = {
        "0" : "ZRO",
        "1" : "ONE",
        "2" : "TWO",
        "3" : "THR",
        "4" : "FOR",
        "5" : "FIV",
        "6" : "SIX",
        "7" : "SVN",
        "8" : "EGT",
        "9" : "NIN",
    }

    for i in range(N):
        arr[i] = txtnum[str(arr[i])]

    print(f'#{tc}')
    print(*arr)