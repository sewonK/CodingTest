# 00:27 ~ 01:07

from collections import deque 

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
INF = 25*25*25*500

def BFS(board):
    queue = deque()
    visit = [[[INF for _ in range(len(board[0]))] for _ in range(len(board[0]))] for _ in range(2)]
    min_price = INF
    x, y, prev, price = 0, 0, '', 0
    visit[0][x][y] = 0
    visit[1][x][y] = 0
    queue.append((x, y, prev, price))
    while queue:
        (curx, cury, prev, price) = queue.popleft()
        if curx == len(board[0])-1 and cury == len(board[0])-1:
            if min_price > price:
                min_price = price
        for i in range(4):
            nextx = curx + dx[i]
            nexty = cury + dy[i]
            if nextx < 0 or nextx >= len(board[0]) or nexty < 0 or nexty >= len(board[0]):
                continue
            if board[nextx][nexty] == 1:
                continue
            #현재 이동 방향 설정
            if dx[i] == 0:
                cur = 0
            else:
                cur = 1
            # 직선 도로일 경우
            if prev == '' or cur == prev:
                add = 100
            # 코너일 경우
            else:
                add = 100 + 500
            if visit[cur][nextx][nexty] > price + add:
                visit[cur][nextx][nexty] = price + add
                queue.append((nextx, nexty, cur, price + add))
    return min_price

def solution(board):
    answer = BFS(board)
    return answer

print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))