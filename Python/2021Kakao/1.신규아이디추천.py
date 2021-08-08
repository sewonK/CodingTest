new_id = "=.="
def solution(new_id):
    answer = ''
    new_id = new_id.lower() #1
    for word in new_id: #2
        if word.isalnum() or word in '-_.':
            answer += word
    
    while '..' in answer:
        answer = answer.replace('..', '.') #3
        
    if (answer[0] == '.'): #4
        answer = answer[1:]
        
    if (len(answer) > 1) and (answer[len(answer)-1] == '.'):
        answer = answer[:len(answer)-1]

    if answer == '': #5
        answer = 'a'
    
    if len(answer) >= 16: #6
        answer = answer[:15]
        if answer[14] == '.':
            answer = answer[:14]
    
    if len(answer) <= 2: #7
        while len(answer) < 3:
            answer += answer[len(answer) - 1]

    return answer

print(solution(new_id))    