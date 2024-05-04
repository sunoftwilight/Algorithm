import math

def solution(N, stations, W):
    answer = 0
    current_position = 1
    station_index = 0
    coverage_range = 2 * W + 1

    while current_position <= N:
        if station_index < len(stations) and stations[station_index] - W <= current_position:
            current_position = stations[station_index] + W + 1
            station_index += 1
        else:
            answer += 1
            current_position += coverage_range

    return answer