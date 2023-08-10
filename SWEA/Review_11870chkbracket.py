def solve(str):
    stack = []

    # 문자열을 스캔
    for i in range(len(str)):   # for ch in str (인덱스 접근할 일 없으면 이렇게도 가능)
        if str[i] == '(' or str[i] == '{':    # 왼쪽 괄호일 때
            stack.append(str[i])

        elif str[i] in [')', '}']:    # 6번 줄과 동일한 의미 (다른 방법)
            if not stack:             # stack이 비어있으면 / is_empty : len(stack) == 0
                return 0              # 오른쪽 검사

            else:
                temp = stack.pop()

                # 같은 종류인지 검사
                if str[i] == ')' and temp != '(':
                    return 0

                elif str[i] == '}' and temp != '{':
                    return 0

    if stack: return 0   # stack에 왼쪽이 남아 있을 경우 len(stack) != 0

    return 1             # 앞의 탐색 모두 통과하면 1 return


T = int(input())

for tc in range(1, T+1):
    str = input()

    print(f'#{tc} {solve(str)}')