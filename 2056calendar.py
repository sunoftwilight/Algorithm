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
        if 1 <= month <= 12:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if 1<= day <= 31:
                    print(true_case)
                else : 
                    print(false_case)
            elif month == 2:
                if 1<= day <= 28:
                    print(true_case)
                else:
                    print(false_case)
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if 1<= day <= 30:
                    print(true_case)
                else :
                    print(false_case)
            else:
                print(false_case)
        else:
            print(false_case)
    else:
        print(false_case)
    