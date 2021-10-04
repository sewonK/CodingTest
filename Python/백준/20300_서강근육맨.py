def solution():
    N = int(input())
    t = list(map(int, input().split()))
    answer = -1
    t.sort()
    if N % 2 == 0:
        for i in range(N//2):
            answer = max(answer, t[i] + t[N - 1 - i])
    else:
        answer = t[N - 1]
        for i in range(N//2):
            answer = max(answer, t[i] + t[N - 2 - i])
    return answer

print(solution())
