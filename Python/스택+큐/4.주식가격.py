prices = [1, 2, 3, 2, 1, 1]

def solution(prices):
    answer = [0 for price in range(len(prices))]
    time = []
    time.append(0)
    next = 1
    while time:
        if next < len(prices):
            while time:
                front = time[len(time) - 1]
                if prices[front] > prices[next]:
                    time.pop()
                    answer[front] = next - front
                else:
                    break
            time.append(next)
        else:
            for i in time:
                answer[i] = next - 1 - i
            break
        next += 1
    return answer

print(solution(prices))