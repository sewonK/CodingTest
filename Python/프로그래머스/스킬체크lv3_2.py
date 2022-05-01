from itertools import permutations

def check(checking_id, banned_id):
    for idx, id in enumerate(banned_id):
        if (len(checking_id[idx]) != len(id)):
            return False
        for i in range(len(id)):
            if(id[i:i+1] == '*'):
                continue
            elif(checking_id[idx][i:i+1] != id[i:i+1]):
                return False
    return True

def solution(user_id, banned_id):
    answer_set = []
    id_list = list(permutations(user_id, len(banned_id)))
    for id in id_list:
        if(check(id, banned_id)):
            id = set(id)
            if (id not in answer_set):
                answer_set.append(id)
        else:
            continue
    return len(answer_set)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))