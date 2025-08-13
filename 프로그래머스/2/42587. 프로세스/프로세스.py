from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque((p, i) for i, p in enumerate(priorities))
    order = 0
    
    while q:
        p, idx = q.popleft()
        if any(p2 > p for p2, _ in q):
            q.append((p, idx))
        else:
            order += 1 #실행
            if (idx == location):
                return order
    
    return answer