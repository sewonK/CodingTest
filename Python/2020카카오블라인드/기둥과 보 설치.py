n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def solution(n, build_frame):
    answer = []
    def check():
        for x, y, kind in answer:
            #0은 기둥, 1은 보
            if kind == 0:                    
                # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
                if (y == 0) or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer: #
                    continue
                else:
                    return False
            elif kind == 1:
                # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                    continue
                else:
                    return False
        return True

    for frame in build_frame:
        x = frame[0]
        y = frame[1]
        kind = frame[2]
        set = frame[3]

        if set: #건축
            answer.append([x, y, kind])
            if(check()):
                continue
            else:
                answer.remove([x, y, kind])    
        else: 
            answer.remove([x, y, kind])
            if(check()):
                continue
            else:
                answer.append([x, y, kind])
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer

print(solution(n, build_frame))