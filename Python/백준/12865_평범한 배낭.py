def solution():
    N, K = map(int, input().split())
    weight = [0 for _ in range(N + 1)] 
    value = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        w, v = map(int, input().split())
        weight[i] = w
        value[i] = v
    
    knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1): #물건 순서
        for j in range(K + 1): #담을 수 있는 용량
            w = weight[i]
            v = value[i]
            
            if j < w: #못담음
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(v + knapsack[i - 1][j - w], knapsack[i-1][j])
    
    return knapsack[N][K]

print(solution())
