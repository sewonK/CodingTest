import heapq

scoville = [1, 1]
K = 7

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and (scoville[0] < K):
        min_first = heapq.heappop(scoville)
        min_second = heapq.heappop(scoville)
        heapq.heappush(scoville, min_first + min_second*2)
        answer += 1
    if scoville[0] < K:
        answer = -1
    return answer
print(solution(scoville, K))