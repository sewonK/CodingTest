# 01:00 ~ 01:44

def solution(msg):
    answer = []
    dict = {}
    for i in range(1, 27):
        dict[chr(64 + i)] = i
    max_num = 26
    idx = 0
    while idx < len(msg):
        n = 1 #n번째 글자
        while msg[idx:idx+n] in dict:            
            if idx+n >= len(msg):
                n += 1                
                break
            n += 1
        if n > 1:
            n -= 1
        answer.append(dict[msg[idx:idx+n]])
        if idx+n < len(msg):
            dict[msg[idx:idx+n]+msg[idx+n]] = max_num + 1
            max_num += 1
        idx += n
    return answer

# print(solution("ABABABABABABABAB"))