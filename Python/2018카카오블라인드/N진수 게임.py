# 11:27 ~ 

def Nnumber(N, number):
    temp = "0123456789ABCDEF"
    q, r = divmod(number, N)
    if q == 0:
        return temp[r]
    else:
        return Nnumber(N, q) + temp[r]

# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
def solution(n, t, m, p):
    answer = ''
    turn, num = 0, 0
    while len(answer) < t:
        result = Nnumber(n, num)
        for r in result:            
            if (turn % m) == p-1:
                answer += r
                if len(answer) == t:
                    break
            turn += 1
        num += 1        
    return answer

print(solution(16, 16, 2, 2))