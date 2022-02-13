# 22:55 ~ 

def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        head_complete = False
        num_idx = 0
        for idx, c in enumerate(file):
            if c.isdigit() and not head_complete:
                head = file[:idx]
                number = file[idx:]
                head_complete = True
                num_idx = idx
            elif not c.isdigit() and head_complete:            
                number = file[num_idx:idx]
                tail = file[idx:]
                break            
        answer.append([head, number, tail])
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(a) for a in answer]

print(solution(["A-10", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14"]))