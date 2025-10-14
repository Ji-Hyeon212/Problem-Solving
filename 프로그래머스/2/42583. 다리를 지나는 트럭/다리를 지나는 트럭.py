from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    waiting = deque(truck_weights)
    curr_weight = 0
    time = 0
    while (curr_weight >0 or waiting):
        time += 1
        passed = bridge.popleft()
        curr_weight -= passed
        if (waiting):
            next_weight = waiting[0]
            if (curr_weight + next_weight <= weight):
                truck = waiting.popleft()
                bridge.append(truck)
                curr_weight += next_weight
            else:
                bridge.append(0)
    return time