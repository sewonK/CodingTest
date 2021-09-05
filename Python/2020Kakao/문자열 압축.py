s = "a"

def solution(s):
    answer = len(s)
    for num in range(1, len(s)//2 + 1):
        word = s[:num]
        cnt = 0
        result = 0
        for i in range(0, len(s), len(word)):
            if word == s[i:i + len(word)]:
                cnt += 1
            else:
                if cnt != 1:
                    result += len(str(cnt)) + len(word)
                else:
                    result += len(word)
                word = s[i:i + len(word)]
                cnt = 1
        if cnt != 1:
            result += len(str(cnt)) + len(word)
        else:
            result += len(word)
        if result < answer:
            answer = result
    return answer

print(solution(s))