orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
# from itertools import combinations
# def solution(orders, course):
#     answer = []
#     for n in course:
#         count = dict()
#         for order in orders:
#             combis = list(combinations(order, n))
#             for combi in combis:
#                 word = ''
#                 combi = sorted(combi)
#                 for char in combi:
#                     word += char
                
#                 if word in count:
#                     count[word] += 1
#                 else:
#                     count[word] = 1
                            
#         max = 0
#         for key, value in count.items():
#             if max < value:
#                 max = value

#         if max >= 2:
#             for key, value in count.items():
#                 if max == value:
#                     answer.append(key)
        
#     answer = sorted(answer)
#     return answer


from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)

print(solution(orders, course))