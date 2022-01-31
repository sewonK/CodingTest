# 23:20 ~ 24:49

def add_zero(music):
    result = ''
    idx = 0
    while(idx < len(music)):
        result += music[idx]
        if music[(idx+1) % len(music)] == '#':
            result += '#'
            idx +=1
        else:
            result += '0'      
        idx += 1
    return result          

def get_play_time(start, end):
    start_hh, start_mm = map(int, start.split(":"))
    end_hh, end_mm = map(int, end.split(":"))
    return (end_hh - start_hh) * 60 + end_mm - start_mm
        
def get_entire_music(music, play_time):
    return music*((play_time*2) // len(music)) + music[:(play_time*2) % len(music)]

def solution(m, musicinfos):
    answer = '(None)'
    max_play_time = -1    
    m = add_zero(m)
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(",")
        music = add_zero(music)        
        play_time = get_play_time(start, end)
        entire_music = get_entire_music(music, play_time)
        idx = entire_music.find(m)
        if (idx != -1) and (max_play_time < play_time):
            max_play_time = play_time
            answer = title
    return answer

# print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))