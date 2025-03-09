from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    lenth = len(queue1)
    total = sum1 + sum2
    #합이 홀수가 되면 중간값이 되도록 만들 수 없음. 정수의 합이니까.
    if total % 2 == 0:
        middle = total//2
    else: return -1
    
    for _ in range(lenth*3):
        if (sum1 > middle):
            e = queue1.popleft()
            queue2.append(e)
            sum1 -= e
            sum2 += e
        elif (sum1 < middle):
            e = queue2.popleft()
            queue1.append(e)
            sum2 -= e
            sum1 += e
        elif (sum1 == middle):
            return answer
        answer += 1
    return -1
