import sys
sys.stdin = open('GNS_test_input.txt', 'r')
sys.stdout = open('GNS_output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    temp = input()   # dummy
    arr = list(map(str, input().split()))
    N = len(arr)

    cnt = [0] * 10

    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    numdict = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9,
    }

    for n in arr:
        cnt[numdict[n]] += 1

    ans = []

    for i in range(10):
        for _ in range(cnt[i]):
            ans.append(num[i])

    print(f'#{tc}', *ans)
