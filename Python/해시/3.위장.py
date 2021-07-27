# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    answer = 1
    category = dict()
    for cloth in clothes:
        if cloth[1] in category:
            category[cloth[1]] +=1 
        else:
            category[cloth[1]] = 1
    for i in category:
        answer *= (category[i] + 1)
        
    return answer - 1

# print(solution(clothes))
# Best 풀이
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer