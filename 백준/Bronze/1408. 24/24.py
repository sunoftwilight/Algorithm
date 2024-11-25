current = input().split(':')
start = input().split(':')

cur_sec = int(current[0]) * 3600 + int(current[1]) * 60 + int(current[2])
stt_sec = int(start[0]) * 3600 + int(start[1]) * 60 + int(start[2])

rmi_sec = 0

if cur_sec < stt_sec:
    rmi_sec = stt_sec - cur_sec

else:
    rmi_sec += stt_sec

    lst_sec = 23 * 3600 + 59 * 60 + 59 + 1
    rmi_sec += lst_sec - cur_sec

h = str(rmi_sec // 3600).zfill(2)
m = str((rmi_sec % 3600) // 60).zfill(2)
s = str((rmi_sec % 3600) % 60).zfill(2)

print(f'{h}:{m}:{s}')
