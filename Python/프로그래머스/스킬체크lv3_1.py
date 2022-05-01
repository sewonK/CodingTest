def MakeGraph(n, edge):
    global graph
    graph = [[] for _ in range(n+1)]
    # 연결
    for vertex in edge:
        graph[vertex[0]].append(vertex[1])
        graph[vertex[1]].append(vertex[0])

def BFS(n):
    global graph, dists
    dists = [0 for _ in range(n+1)]
    visit = [False for _ in range(n+1)]
    queue = [[1, 0]]
    visit[1] = True
    while(len(queue) > 0):
        cur_node = queue[0][0]
        cur_dist = queue.pop(0)[1]
        dists[cur_node] = cur_dist
        for next_node in graph[cur_node]:
            if (visit[next_node]):
                continue
            visit[next_node] = True
            next_dist = cur_dist + 1
            queue.append([next_node, next_dist])

def GetAnswer(n):
    global dists
    answer = 0
    max_dist = max(dists)
    for dist in dists:
        if(max_dist == dist):
            answer += 1
    return answer

def solution(n, edge):
    MakeGraph(n, edge)
    BFS(n)
    answer = GetAnswer(n)
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))