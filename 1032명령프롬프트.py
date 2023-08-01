T = int(input())

inputs = []                               # 입력받을 문자열이 삽입될 리스트
for i in range(T):
    inputs.append(input())                # 반복문을 통해 T의 개수만큼 문자열 입력받음

for test_case in range(1, T+1):

    pattern = []                          # 문자열의 패턴이 삽입될 리스트

    if T==1:
        pattern = inputs                  # 문자열이 1개일 때는 자신을 그대로 리스트에 삽입

    for k in range(len(inputs[0])):       # 입력된 문자열 중 첫번째 문자열(0번)을 기준으로 설정
        spell = inputs[0][k]              # 기준 문자열을 통해 spell이라는 비교 인자를 설정
        for idx in range(1,T):            # 동일한 자릿수에 대해 입력받은 문자열 리스트를 순회하며 spell과 동일한지 비교
            if spell == inputs[idx][k]:   # 동일한 경우에는 별다른 동작없이 반복문 순회하며 마지막 문자열까지 비교
                if idx == (T-1):          # 만약 마지막 문자열까지 해당 자릿수의 문자가 같다면
                    pattern.append(spell) # 패턴 리스트에 해당 자릿수의 문자 삽입
            else:                         # 만약 동일하지 않다면
                pattern.append('?')       # 패턴 리스트에 ? 삽입 후 반복 종료
                break                     #     => 문자열 리스트 중 해당 자릿수가 동일하지 않은 문자열이 하나라도 있다면 뒤의 문자열은 비교할 필요 X 

print(''.join(pattern))                   # 패턴 리스트는 문자 하나하나를 요소로 넣어둔 상태이므로 .join() 메소드를 통해 하나의 문자열로 결합
