participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
def solution(participant, completion):
    answer = ''
    cnt = dict()
    for i in participant:
        if (i in cnt):
            cnt[i] += 1
        else :
            cnt[i] = 1
    for i in completion:
        if (i in cnt):
            cnt[i] -= 1
        else :
            cnt[i] = 0
    for i in cnt:
        if(cnt[i] > 0):
            answer = i
    return answer
# print(solution(participant, completion))

# Best 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# print(solution(participant, completion))