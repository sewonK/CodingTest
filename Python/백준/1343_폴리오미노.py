def checkCnt(cnt):
    result = ''
    cnt_A = 0
    cnt_B = 0
    while(cnt > 0):
        if cnt % 4 == 0:
            cnt_A += (cnt//4)
            cnt %= 4
        elif cnt % 2 == 0:
            cnt_B += 1
            cnt -= 2
        else:
            return result
    for _ in range(cnt_A):
        result += 'AAAA'
    for _ in range(cnt_B):
        result += 'BB'
    return result

def solution():
    board = input()
    answer = ''
    cnt = 0
    for char in board:
        if char == '.':
            if cnt > 0 :             
                tmp = checkCnt(cnt)
                if tmp == '':
                    return -1
                answer += tmp
                cnt = 0
            answer += '.'
        else:
            cnt += 1           
    if cnt > 0: 
        tmp = checkCnt(cnt)
        if tmp == '':
            return -1
        answer += tmp
        
    if answer == '':
        answer = -1
    return answer
print(solution())