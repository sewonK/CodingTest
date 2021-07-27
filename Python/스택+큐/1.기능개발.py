from collections import deque
import math
progresses = [99, 99, 99, 99, 99, 99]
speeds = [1, 1, 1, 1, 1, 1]
def solution(progresses, speeds):
    answer = []
    workday = deque([])
    for progress, speed in zip(progresses, speeds):
        workday.append(math.ceil((100 - progress) / speed))
    
    idx = -1
    max = 0
    while workday:
        cur = workday.popleft()
        if(max < cur):
            max = cur
            idx += 1
            answer.append(1) #새로운 배포 시작
        else:
            answer[idx] += 1 
        
    return answer

print(solution(progresses, speeds))