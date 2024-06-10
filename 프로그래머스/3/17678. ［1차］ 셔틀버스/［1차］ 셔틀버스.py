def solution(n, t, m, timetable):
    answer = ''

    bus_time = []
    for i in range(n):
        bus_time.append(9 * 60 + t * i)

    crew_time = []
    for j in range(len(timetable)):
        crew_time.append(int(timetable[j][:2]) * 60 + int(timetable[j][3:]))
    crew_time.sort()

    i = 0                                        # 다음에 버스에 오를 크루의 인덱스
    for bus in bus_time:
        cnt = 0                                  # 버스에 타는 크루 수
        while cnt < m and i < len(crew_time) and crew_time[i] <= bus:
            i += 1
            cnt += 1

        if cnt < m:                              # 버스에 자리가 남았을 경우
            answer = bus

        else:                                    # 버스에 자리가 없는 경우
            answer = crew_time[i - 1] - 1        # 맨 마지막 크루보다 1분 먼저 도착

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)
