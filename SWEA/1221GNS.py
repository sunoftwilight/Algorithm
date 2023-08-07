import sys
sys.stdin = open('GNS_test_input.txt', 'r')
sys.stdout = open('GNS_output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    temp = input()   # dummy
    arr = list(map(str, input().split()))

    print(arr)