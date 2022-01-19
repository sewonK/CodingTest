# 17:20 ~ 17:40

def solution(id_list, report, k):
    answer = []
    list = dict() #사람: 인덱스
    report_list = dict() 
    report_num_list = dict() 
    for idx, id in enumerate(id_list):
        answer.append(0)
        list[id] = idx
        report_list[id] = []
        report_num_list[id] = 0
    for r in report:
        reporter, reportee = r.split() 
        if reporter not in report_list[reportee]: #신고는 동일인물에 한해 1번만 가능
            report_list[reportee].append(reporter) #신고당한사람: 신고한사람
            report_num_list[reportee] += 1 #신고당한사람: 횟수
    for reportee, num in report_num_list.items():
        if num >= k: #k번이상 신고당한 사람이면
            for reporter in report_list[reportee]: #이사람을 신고한 사람을 찾아서
                answer[list[reporter]] += 1 #answer에 +1 해준다

    return answer

# print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"], 3))