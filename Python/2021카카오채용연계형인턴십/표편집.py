# 22:00 ~ 23:06
import heapq

def solution(n, k, cmds):
    answer = ''
    #left의 루트노드는 선택된 행이다
    left, right, delete, result = [], [], [], []
    for i in range(k + 1):
        heapq.heappush(left, -i)
    for i in range(k + 1, n):
        heapq.heappush(right, i)
    for cmd in cmds:
        if cmd == 'C':
            delete.append(-heapq.heappop(left))
            if right:
                heapq.heappush(left, -heapq.heappop(right))                  
        elif cmd == 'Z':
            d = delete.pop()
            if -left[0] < d:
                heapq.heappush(right, d)
            else:
                heapq.heappush(left, -d)
        else:
            c, x = cmd.split()
            if c == 'U':
                for _ in range(int(x)):
                    heapq.heappush(right, -heapq.heappop(left))                
            elif c == 'D':
                for _ in range(int(x)):
                    heapq.heappush(left, -heapq.heappop(right))                         
    
    while left:
        heapq.heappush(result, (-heapq.heappop(left)))
    while right:
        heapq.heappush(result, (heapq.heappop(right)))
    
    for i in range(n):
        if (not result) or (i != result[0]):
            answer += 'X'
            continue
        else:
            answer += 'O'
            heapq.heappop(result)

    return answer

# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))