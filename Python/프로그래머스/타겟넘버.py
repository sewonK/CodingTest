def DFS(numbers, target, idx, sum):
    global answer
    if (idx >= len(numbers)):
        if (sum == target):
            answer += 1
        return
    DFS(numbers, target, idx+1, sum+numbers[idx])
    DFS(numbers, target, idx+1, sum-numbers[idx])


def solution(numbers, target):
    global answer
    answer = 0
    DFS(numbers, target, 0, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))