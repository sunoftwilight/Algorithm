grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

major = [input() for _ in range(20)]
total = 0
cnt = 0

for i in range(20):
    this = major[i].split()[1:]

    if this[1] != 'P':
        total += float(this[0]) * grade[this[1]]
        cnt += float(this[0])

print(total / cnt)