import math


def solution(fees, records):
    car_cost = []
    END = 23 * 60 + 59
    
    cars = {}
    
    for record in records:
        time, car, io = record.split(' ')
        car = int(car)
        h, m = map(int, time.split(':'))
        
        if cars.get(car):
            cars[car].append((h * 60 + m, io))
        else:
            cars[car] = [(h * 60 + m, io)]
    
    for key, value in cars.items():
        n = len(value)
        tmp_time = 0
        
        for i in range(0, n - 1, 2):
            tmp_time += value[i + 1][0] - value[i][0]
        
        if n % 2:
            tmp_time += END - value[-1][0]
        
        cost = fees[1]
        
        if tmp_time > fees[0]:
            cost += math.ceil((tmp_time - fees[0]) / fees[2]) * fees[3]
        
        car_cost.append([key, cost])
    
    car_cost.sort()
    
    answer = []
    for car, cost in car_cost:
        answer.append(cost)
    
    return answer