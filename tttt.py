events = {
    'No Events': 0,
    'Rain': 0,
    'Thunderstorm': 0,
    'Fog': 0,
    'Snow': 0,
}

for i in range(21):
    evt = input()
    if evt == ' ' or '':
        events['No Events'] += 1

    elif ',' in evt:
        evt_list = evt.split(' , ')

        for j in range(len(evt_list)):
            events[evt_list[j]] += 1

    else:
        events[evt] += 1

print(events)