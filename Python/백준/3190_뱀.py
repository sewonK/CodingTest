from collections import deque

def move(N, K, L, board, s, dir):
    dirx = [0, 1, 0, -1] #우하좌상
    diry = [1, 0, -1, 0]
    headx, heady = 1, 1
    snake = deque()

    ###초기값 대입###
    board[headx][heady] = 1
    snake.append([headx, heady])
    idx = 0
    d = 0 #우
    answer = 0
    ###시뮬레이션###
    while(1):
        tailx, taily = snake[0][0], snake[0][1]
        # 뱀 이동
        headx, heady = headx + dirx[d], heady + diry[d]
        # 벽을 만나거나 자신의 몸을 만나면 끝
        if (headx > N) or (heady > N) or (headx <= 0) or (heady <= 0) or (board[headx][heady] == 1):
            return answer + 1
        
        #이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if board[headx][heady] == 2:
            board[headx][heady] = 1
            snake.append([headx, heady])

        # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.    
        elif board[headx][heady] == 0:
            board[tailx][taily] = 0
            snake.popleft()
            board[headx][heady] = 1
            snake.append([headx, heady])
        
        answer += 1

        ### 방향 바꾸기
        if idx < L and answer == s[idx]:
            if dir[idx] == 'D': #오른쪽 우 하 좌 상
                d += 1
                d = d % 4
            elif dir[idx] == 'L': #왼쪽 우 상 좌 하
                d -= 1
                d = (d + 4) % 4
            idx += 1
    
    return answer

def solution():
    answer = 0
    ###INPUT###
    N = int(input())
    board = [[0] * (N + 1) for _ in range(N + 1)]
    K = int(input())
    for i in range(K):
        x, y = map(int, input().split())
        board[x][y] = 2 #사과가 있으면 2
    L = int(input())
    s = [0 for _ in range(L)]
    dir = ['' for _ in range(L)]
    for i in range(L):
        s[i], dir[i] = input().split()
        s[i] = int(s[i])
    
    ###시뮬레이션###
    answer = move(N, K, L, board, s, dir)
    return answer

print(solution())
