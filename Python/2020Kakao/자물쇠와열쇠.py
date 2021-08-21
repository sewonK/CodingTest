key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
import copy

def setLock(M, N, board, lock):
    for i in range(N):
        for j in range(N):
            board[i+M][j+M] = lock[i][j]

def lotateKey(M, key): #(x, y) -> (y, M - 1 - x), 시계방향으로 90도
    newKey = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            newKey[j][M-1-i] = key[i][j]
    return newKey
#return list(zip(*key[::-1]))

def putKey(x, y, M, checkBoard, key):
    for i in range(M):
        for j in range(M):
                checkBoard[i + x][j + y] += key[i][j]

def check(M, N, checkBoard):
    for i in range(N):
        for j in range(N):
            if checkBoard[i+M][j+M] != 1:
                return False
    return True

def solve(M, N, key, lock, board):
    for lotate in range(4):
        key = lotateKey(M, key)
        for i in range(1, M+N):
            for j in range(1, M+N):
                checkBoard = copy.deepcopy(board)
                putKey(i, j, M, checkBoard, key)
                if check(M, N, checkBoard):
                    return True
    return False

def solution(key, lock):
    answer = True
    M, N = len(key), len(lock)
    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    setLock(M, N, board, lock)
    answer = solve(M, N, key, lock, board)
    return answer

print(solution(key, lock))    