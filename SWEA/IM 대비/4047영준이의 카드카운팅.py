T = int(input())

for tc in range(1, T+1):
    card = input()

    pattern = {
        'S': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'],
        'D': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'],
        'H': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'],
        'C': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'],
    }

    flag = 0

    for i in range(0, len(card), 3):
        if card[i+1:i+3] not in pattern[card[i]]:
            flag = 1
            break
        pattern[card[i]].remove(card[i+1:i+3])

    if flag:
        print(f'#{tc} {"ERROR"}')
    else:
        print(f'#{tc} {len(pattern["S"])} {len(pattern["D"])} {len(pattern["H"])} {len(pattern["C"])}')
