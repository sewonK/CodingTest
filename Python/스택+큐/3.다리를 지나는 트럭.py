from collections import deque
bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

def solution(bridge_length, weight, truck_weights):
    #초기화
    answer = 0
    trucks_in_bridge = deque([])
    waiting_truck = deque([idx, truck_weight] for idx, truck_weight in enumerate(truck_weights))
    time = [0 for i in range(10001)]
    
    #1번 트럭 다리에 넣어주는 로직
    trucks_in_bridge.append([0, truck_weights[0]])
    waiting_truck.popleft()
    total = truck_weights[0]
    
    while trucks_in_bridge:
        cur = trucks_in_bridge[0]
        if time[cur[0]] >= bridge_length: #다리 다 건넘
            total -= cur[1]
            trucks_in_bridge.popleft()
        if waiting_truck:
            next = waiting_truck[0]
            if total + next[1] <= weight: #새로운 트럭 들어옴
                total += next[1]
                trucks_in_bridge.append(next)
                waiting_truck.popleft()
        for truck in trucks_in_bridge: #1초 경과
            time[truck[0]] += 1
        answer += 1 
    return answer

print(solution(bridge_length, weight, truck_weights))
