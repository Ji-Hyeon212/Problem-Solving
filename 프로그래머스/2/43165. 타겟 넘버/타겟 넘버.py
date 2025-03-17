def solution(numbers, target):
    answer = 0
    stack = [[numbers[0],0], [-1*numbers[0], 0]]
    while stack:
        value, idx = stack.pop()
        idx+=1
        if idx < len(numbers):
            stack.append([value-numbers[idx],idx])
            stack.append([value+numbers[idx],idx])
        else:
            if value == target:
                answer+=1
    return answer