# 16:16 ~ 16:52
# 플로이드 와샬 알고리즘
INF = 100000*200*200

def graphInit(n):
    global graph 
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                graph[i][j] = 0

def floyd(n):
    global graph
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

def solution(n, s, a, b, fares):
    answer = INF
    global graph 
    graphInit(n)
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
    floyd(n)
    for i in range(1, n + 1):
        if answer > graph[s][i] + graph[i][a] + graph[i][b]:
            answer = graph[s][i] + graph[i][a] + graph[i][b]
    return answer

# print(solution(6, 4, 5, 6, 	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))