T = int(input())

for test_case in range(1, T + 1):
    date = str(input())
    
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])

    _year = str(year).zfill(4)
    _month = str(month).zfill(2)
    _day = str(day).zfill(2)

    true_case = f"#{test_case} {_year}/{_month}/{_day}"
    false_case = f"#{test_case} -1"
    
    if year > 0 :
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day in range(1, 32):
                    print(true_case)
            else : 
                    print(false_case)
        elif month == 2:
            if day in range(1, 29):
                    print(true_case)
            else:
                    print(false_case)
        elif month in [4, 6, 9,11]:
            if day in range(1,31):
                    print(true_case)
            else :
                    print(false_case)
        else:
                print(false_case)
    else:
            print(false_case)
