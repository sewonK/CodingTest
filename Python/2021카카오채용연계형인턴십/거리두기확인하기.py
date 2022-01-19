# 15:29 ~ 16:00
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(place, x, y):
    queue = deque()
    visit = [[False for _ in range(5)] for _ in range(5)]
    queue.append((x, y, 0))
    visit[x][y] = True
    while(queue):
        x = queue[0][0]
        y = queue[0][1]
        dist = queue[0][2]
        queue.pop()
        if dist > 1:
            continue
        for k in range(4):
            nextx = x + dx[k]
            nexty = y + dy[k]
            if nextx < 0 or nextx >= 5 or nexty < 0 or nexty >= 5:
                continue
            if visit[nextx][nexty] or place[nextx][nexty] == 'X':
                continue
            if place[nextx][nexty] == 'P':
                return False
            if place[nextx][nexty] == 'O':
                visit[nextx][nexty] = True
                queue.append((nextx, nexty, dist + 1))


def check(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == 'P':
                if (BFS(place, x, y) == False):
                    return False
    return True
                
def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))