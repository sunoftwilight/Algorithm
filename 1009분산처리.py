T = int(input())

for test_case in range(1, T+1):
    a, b = map(int, input().split())

    data_num = a ** b

    digit_list = list(str(data_num))
    N = len(digit_list)-1
    last_digit = digit_list[N]

    print(int(last_digit))