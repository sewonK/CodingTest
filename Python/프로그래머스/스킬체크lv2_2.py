def BFS(n, start_node):
    global graph
    visit = [[0 for _ in range(n+1)] for _ in range(n+1)]
    queue = [start_node]
    num = 0

    while(len(queue) > 0):
        cur_node = queue.pop(0)
        num += 1
        for next_node, val in enumerate(graph[cur_node]):
            # 연결 안되어있거나 이미 방문한 노드
            if (val == 0) or (visit[cur_node][next_node] == 1):
                continue

            visit[cur_node][next_node] = 1
            visit[next_node][cur_node] = 1
            queue.append(next_node)

    return num

def solution(n, wires):
    answer = 101
    global graph
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for wire in wires:
        # 노드 간 연결
        graph[wire[0]][wire[1]] = 1
        graph[wire[1]][wire[0]] = 1
        
    for wire in wires:
        # 노드 간 연결 끊기
        graph[wire[0]][wire[1]] = 0
        graph[wire[1]][wire[0]] = 0
        

        result = BFS(n, wire[0])
        left = n - result
        answer = min(abs(result-left), answer)

        # 다시 연결
        graph[wire[0]][wire[1]] = 1
        graph[wire[1]][wire[0]] = 1

    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))