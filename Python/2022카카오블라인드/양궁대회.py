# 21:16 ~ 23:00
# 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요. < 부분에서 계속 오류남
# 가장 낮은 점수부터 확인하고, return 하도록 했어야 했는데 ...
# 큰 점수부터 확인해서 2개의 테스트 케이스가 오류가 났다.

def calcPoint(apeach, lion):
    apeach_score = 0
    lion_score = 0
    for i in range(11):
        if apeach[i] == lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            apeach_score += 10 - i
        else:
            lion_score += 10 - i
    return lion_score - apeach_score

# 지금쏘는 과녁 idx, 남은 화살 개수, 어피치점수, 내점수
def DFS(idx, n, apeach, lion):
    global answer, point
    if n < 0:
        return
    #점수 계산
    if idx > 10:
        diff = calcPoint(apeach, lion)
        if diff <= 0:
            return
        if diff > point:
            point = diff
            answer = [lion[i] for i in range(11)]
            answer[10] += n            
        return

    #상대가 쏜 점수보다 높이 쏴본다
    lion[10-idx] = apeach[10-idx]+1
    DFS(idx+1, n-lion[10-idx], apeach, lion)
    lion[10-idx] = 0
    DFS(idx+1, n, apeach, lion)

def solution(n, info):
    global answer, point
    answer = [-1]
    point = 0
    DFS(0, n, info, [0 for _ in range(11)])
    return answer

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# 테스트 1 〉	통과 (0.16ms, 10.3MB)
# 테스트 2 〉	통과 (2.24ms, 10.3MB)
# 테스트 3 〉	통과 (2.09ms, 10.3MB)
# 테스트 4 〉	통과 (1.64ms, 10.2MB)
# 테스트 5 〉	통과 (2.41ms, 10.3MB)
# 테스트 6 〉	통과 (4.19ms, 10.3MB)
# 테스트 7 〉	통과 (0.91ms, 10.2MB)
# 테스트 8 〉	통과 (0.64ms, 10.3MB)
# 테스트 9 〉	통과 (1.32ms, 10.3MB)
# 테스트 10 〉	통과 (0.35ms, 10.3MB)
# 테스트 11 〉	통과 (0.56ms, 10.2MB)
# 테스트 12 〉	통과 (0.82ms, 10.3MB)
# 테스트 13 〉	통과 (1.60ms, 10.2MB)
# 테스트 14 〉	통과 (2.13ms, 10.2MB)
# 테스트 15 〉	통과 (2.32ms, 10.3MB)
# 테스트 16 〉	통과 (1.20ms, 10.2MB)
# 테스트 17 〉	통과 (0.87ms, 10.2MB)
# 테스트 18 〉	통과 (0.15ms, 10.2MB)
# 테스트 19 〉	통과 (0.05ms, 10.3MB)
# 테스트 20 〉	통과 (2.07ms, 10.2MB)
# 테스트 21 〉	통과 (2.12ms, 10.3MB)
# 테스트 22 〉	통과 (2.39ms, 10.3MB)
# 테스트 23 〉	통과 (0.67ms, 10.2MB)
# 테스트 24 〉	통과 (2.26ms, 10.4MB)
# 테스트 25 〉	통과 (3.40ms, 10.3MB)