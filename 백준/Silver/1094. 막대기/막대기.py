X = int(input())

sticks = []
init = 64

while init > 0:
    sticks.append(init)
    init //= 2

answer = [0, 0]

for stick in sticks:
    if stick + answer[0] <= X:
        answer[0] += stick
        answer[1] += 1

print(answer[1])
