def solution(n, stations, w):
    answer = 0

    scopes = [(0, 0)]
    for station in stations:
        scopes.append((station - w, station + w))
    scopes += [(n+1, n+1)]

    cover = 2 * w + 1
    for i in range(1, len(scopes)):
        empty = scopes[i][0] - scopes[i - 1][1] - 1
        if empty <= 0:
            continue

        share, remainder = divmod(empty, cover)
        answer += share
        if remainder:
            answer += 1

    return answer


# by GPT
# import math

# def solution(N, stations, W):
#     answer = 0
#     current_position = 1
#     station_index = 0
#     coverage_range = 2 * W + 1

#     while current_position <= N:
#         if station_index < len(stations) and stations[station_index] - W <= current_position:
#             current_position = stations[station_index] + W + 1
#             station_index += 1
#         else:
#             answer += 1
#             current_position += coverage_range

#     return answer
