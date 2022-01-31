# 02:45 ~ 03:14

def set_dic(gems):
    result = {}
    for gem in gems:
        result[gem] = 0
    return result

def solution(gems):
    answer = []
    min_val = 100000
    dic = set_dic(gems)    
    #초기값 설정
    start, end = 0, 0
    dic[gems[start]] += 1
    check_num = 1
    while True:
        if check_num == len(dic):
            if min_val > end-start:
                min_val = end-start
                answer = [start+1, end+1]
            #start 포인터 값 제외
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                check_num -= 1
            #start 포인터 한 칸 앞으로
            start += 1
            if start >= len(gems):
                break
        else:
            #end 포인터 한 칸 앞으로
            end += 1
            if end >= len(gems):
                break
            #end 포인터 값 추가
            dic[gems[end]] += 1
            if dic[gems[end]] == 1:
                check_num += 1
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))