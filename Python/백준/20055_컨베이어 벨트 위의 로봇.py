from collections import deque
def solution():
    N, K = map(int, input().split())
    A = deque(list(map(int, input().split())))

    robot = deque([0 for _ in range(N)])
    K_cnt = 0
    answer = 0
    
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 
    while(K_cnt < K):
        answer += 1
        # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        A.rotate(1)
        robot.rotate(1)
        robot[N-1] = 0
        # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        for i in range(N - 1, -1, -1):
            if robot[i] == 0: #로봇이 없는 경우
                continue
            next = i + 1

            # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
            if robot[next] == 0 and A[next] >= 1:
                robot[next] = robot[i]
                robot[i] = 0
                A[next] -= 1
                
                if A[next] == 0:
                    K_cnt += 1
                    A[next] = -1

                if next == N - 1:
                    robot[next] = 0
                                                    
        # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if A[0] >= 1:
            robot[0] = 1    
            A[0] -= 1
            if A[0] == 0:
                K_cnt += 1
                A[0] = -1

    return answer
    
print(solution())