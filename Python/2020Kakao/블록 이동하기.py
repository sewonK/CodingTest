board = [[0, 0, 0, 1, 1]
        ,[0, 0, 0, 1, 0]
        ,[0, 1, 0, 1, 1]
        ,[1, 1, 0, 0, 1]
        ,[0, 0, 0, 0, 0]]	

from collections import deque
def BFS(N, visit):
    #first, second기준 회전 + 상하좌우
    dirx1 = [0, 0, 1, -1, -1, 1, 0, 0] # first 
    diry1 = [0, 0, 1, 1, 0, 0, -1, 1]
    dirx2 = [1, -1, 0, 0, -1, 1, 0, 0] # second
    diry2 = [-1, -1, 0, 0, 0, 0, -1, 1]
    chkx = [1, -1, 1, -1] #장애물 없는지 체크
    chky = [1, 1, -1, -1]
    
    
    first = [0, 0]
    second = [0, 1]
    visit[0][0][0] = 0
    visit[0][0][1] = 0

    queue = deque()
    queue.append([first, second, 0])
    idx = 0
    while(queue):
        x1, y1 = queue[0][0][0], queue[0][0][1]
        x2, y2 = queue[0][1][0], queue[0][1][1]
        time = queue[0][2]
        queue.popleft()
        
        for i in range(8): 
            nextx1, nexty1 = x1 + dirx1[i], y1 + diry1[i]
            nextx2, nexty2 = x2 + dirx2[i], y2 + diry2[i]
            if (nextx1 >= N) or (nexty1 >= N) or (nextx1 < 0) or (nexty1 < 0):
                continue
            if (nextx2 >= N) or (nexty2 >= N) or (nextx2 < 0) or (nexty2 < 0):
                continue
            if (board[nextx1][nexty1] == 1) or (board[nextx2][nexty2] == 1):
                continue
            if i < 4:
                if i < 2: #first기준 회전
                    checkx, checky = x1 + chkx[i], y1 + chky[i]
                else: #second기준 회전
                    checkx, checky = x2 + chkx[i], y2 + chky[i]
                if (checkx >= N) or (checky >= N) or (checkx < 0) or (checky < 0):
                    continue
                if (board[checkx][checky] == 1):
                    continue
                        
            #first와 second 중 하나라도 안간 곳이 있으면 간다
            if (visit[time][nextx1][nexty1] == -1) or (visit[time][nextx2][nexty2] == -1): 
                if visit[time][nextx1][nexty1] == -1:
                    visit[time+1][nextx1][nexty1] = time + 1
                if visit[time][nextx2][nexty2] == -1:
                    visit[time+1][nextx2][nexty2] = time + 1
                
                
                # 둘 중 한곳이라도 종착지면 리턴
                if ((nextx1 == N-1) and (nexty1 == N-1)) or ((nextx2 == N-1) and (nexty2 == N-1)):
                    return time + 1
                queue.append([[nextx1, nexty1], [nextx2, nexty2], time + 1])
    return -1

def solution(board):
    answer = 0
    N = len(board[0])
    visit = [[[-1 for _ in range(N)] for _ in range(N)] for _ in range(2*N)]
    answer = BFS(N, visit)
    
    return answer

print(solution(board))