# 01:00 ~ 01:44

def solution(msg):
    answer = []
    dict = {}
    for i in range(26):
        dict[chr(65 + i)] = i + 1
    cur, next = 0, 0 #현재 글자 idx, next글자 idx
    while True:
        next += 1
        if next == len(msg):
            answer.append(dict[msg[cur:next]])
            break
        if msg[cur:next+1] not in dict:
            dict[msg[cur:next+1]] = len(dict)+1
            answer.append(dict[msg[cur:next]])
            cur = next
        
    return answer

print(solution("ABABABABABABABAB"))