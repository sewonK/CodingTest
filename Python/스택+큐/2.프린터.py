from collections import deque
priorities = [4, 1, 3, 2]
location = 2
def solution(priorities, location):
    answer = 0
    order = deque([])
    results = []
    for i in range(0, len(priorities)):
        order.append([i, priorities[i]])
    
    while order:
        Print = True
        cur = order[0]
        for i in order:
            if (cur[1] < i[1]):
                #나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
                order.popleft()
                order.append(cur) 
                Print = False
                break                   
        if (Print): #대기열에 J를 넣지 않았으면 J를 인쇄
            results.append(cur)
            order.popleft()

    for result in results:
        answer += 1
        if (location == result[0]):
            break
    return answer

print(solution(priorities, location))