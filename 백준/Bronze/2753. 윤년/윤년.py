year = int(input())
is_yun = False

if year % 4 == 0 and (year % 100 or year % 400 == 0):
    is_yun = True

print(1 if is_yun else 0)
