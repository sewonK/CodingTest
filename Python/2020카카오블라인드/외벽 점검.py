n = 12
weak = [0, 6]
dist = [3]

from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_length = len(weak)
    for i in range(weak_length):
        weak.append(weak[i] + n)
    
    permutate = list(permutations(dist, len(dist)))
    for i in range(weak_length):
        start = [weak[j] for j in range(i, i + weak_length)] #[1, 5, 6, 10]
        for p in permutate: #[1, 2, 3, 4]
            friends = 1
            idx = 0
            check_length = start[0] + p[idx] #2
            for k in range(len(start)):
                if start[k] > check_length:
                    friends += 1
                    if friends > len(dist):
                        break
                    idx += 1
                    check_length = start[k] + p[idx]
            
            answer = min(answer, friends)

    if answer > len(dist):
        answer = -1
    return answer

print(solution(n, weak, dist))