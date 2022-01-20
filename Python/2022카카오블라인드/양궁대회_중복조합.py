from itertools import combinations_with_replacement as combis
from collections import Counter

def combination(n, info):
    global answer, max_point
    # 0 ~ 11까지 n개 중복조합 뽑기 ex.(1, 1, 1, 1, 1)
    for combi in combis(range(11), n):
        #Counter를 통해 각 원소의 개수 구하기 ex.Counter({1: 5})
        cnt = Counter(combi)
        apeach, lion = 0, 0
        #점수계산
        for i in range(11):
            if info[10-i] < cnt[i]:
                lion += i
            elif info[10-i] > 0:
                apeach += i
        if lion-apeach > max_point:
            max_point = lion-apeach
            for i in range(11):
                answer[10-i] = cnt[i] 

def solution(n, info):
    global answer, max_point
    answer = [0]*11
    max_point = 0
    combination(n, info)
    if max_point == 0:
        answer = [-1]
    return answer

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# 테스트 1 〉	통과 (0.26ms, 10.3MB)
# 테스트 2 〉	통과 (326.53ms, 10.3MB)
# 테스트 3 〉	통과 (337.32ms, 10.2MB)
# 테스트 4 〉	통과 (10.38ms, 10.2MB)
# 테스트 5 〉	통과 (676.04ms, 10.2MB)
# 테스트 6 〉	통과 (684.01ms, 10.3MB)
# 테스트 7 〉	통과 (10.52ms, 10.2MB)
# 테스트 8 〉	통과 (1.05ms, 10.3MB)
# 테스트 9 〉	통과 (10.54ms, 10.2MB)
# 테스트 10 〉	통과 (1.09ms, 10.1MB)
# 테스트 11 〉	통과 (3.53ms, 10.2MB)
# 테스트 12 〉	통과 (3.55ms, 10.2MB)
# 테스트 13 〉	통과 (67.35ms, 10.2MB)
# 테스트 14 〉	통과 (366.51ms, 10.2MB)
# 테스트 15 〉	통과 (371.82ms, 10.2MB)
# 테스트 16 〉	통과 (28.93ms, 10.3MB)
# 테스트 17 〉	통과 (11.19ms, 10.3MB)
# 테스트 18 〉	통과 (0.27ms, 10.4MB)
# 테스트 19 〉	통과 (0.07ms, 10.2MB)
# 테스트 20 〉	통과 (377.07ms, 10.3MB)
# 테스트 21 〉	통과 (380.21ms, 10.3MB)
# 테스트 22 〉	통과 (796.91ms, 10.2MB)
# 테스트 23 〉	통과 (1.02ms, 10.2MB)
# 테스트 24 〉	통과 (648.74ms, 10.2MB)
# 테스트 25 〉	통과 (646.38ms, 10.3MB)