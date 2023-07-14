T = int(input())

for test_case in range(1, T + 1):
    date = str(input())
    
    year = int(date[:3])
    month = int(date[4:5])
    day = int(date[6:7])
    
    if year > 0 :
        if 1 <= month <= 12:
            if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
                if day == 31:
                    print(f"#{test_case} {year}/{month}/{day}")
                else : 
                    print(-1)
            elif month == 2:
                if day == 28:
                    print(f"#{test_case} {year}/{month}/{day}")
                else:
                    print(-1)
            elif month == (4 or 6 or 9 or 11):
                if day == 30:
                    print(f"#{test_case} {year}/{month}/{day}")
                else :
                    print(-1)
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)
    
    