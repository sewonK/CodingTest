from collections import defaultdict
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    users = defaultdict(list)
    
    def dfs(user, idx, result, score):
        if idx > 3:
            users[result].append(int(score))
            return result
        
        temp = result
        result += user[idx][0]
        dfs(user, idx+1, result, score)

        result = temp
        result += '-'
        dfs(user, idx+1, result, score)

    def binarySearch(value, score):
        start = 0
        end = len(value)
        while (start < end):
            mid = (start + end) // 2
            if value[mid] < score:
                start = mid + 1
            else:
                end = mid
        return start

    for information in info:
        user = information.split(' ')
        score = user[4]
        user = user[:4]
        
        dfs(user, 0, '', score)
    
    #오름차순 정렬
    for key, value in users.items():
        users[key] = sorted(value)

    for q in query:
        q = q.split(' ')
        question = ''
        score = 0
        for word in q:
            if (word != 'and') and (word.isalpha() or word == '-'):
                question += word[0]
            elif word.isnumeric():
                score = int(word)

        value = users[question]
        cnt = len(value) - binarySearch(value, score)
        answer.append(cnt)
    return answer

print(solution(info, query))