def solution(m, musicinfos):
    answer = []
    idx = 0
    
    m = m.replace('C#', 'H')
    m = m.replace('D#', 'I')
    m = m.replace('F#', 'J')
    m = m.replace('G#', 'K')
    m = m.replace('A#', 'L')
    m = m.replace('B#', 'M')
    
    for music in musicinfos:
        start, end, title, melody = music.split(',')
        
        melody = melody.replace('C#', 'H')
        melody = melody.replace('D#', 'I')
        melody = melody.replace('F#', 'J')
        melody = melody.replace('G#', 'K')
        melody = melody.replace('A#', 'L')
        melody = melody.replace('B#', 'M')
        
        tmpS = start.split(':')
        tmpE = end.split(':')
        
        start = int(tmpS[0]) * 60 + int(tmpS[1])
        end = int(tmpE[0]) * 60 + int(tmpE[1])
        
        duration = end - start
        melodyLen = len(melody)
        
        play = ''
        if melodyLen <= duration:
            quo, remain = divmod(duration, melodyLen)
            play = melody * quo + melody[: remain]
        else:
            play = melody[:duration]
        
        if m in play:
            answer.append((duration*(-1), idx, title))
            idx += 1
    
    if answer:
        answer.sort()
        return answer[0][-1]
    
    return "(None)"