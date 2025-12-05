from collections import deque 

def solution(n, edge):
    # 인접리스트로 그래프 구축
    graph = [[] for _ in range(n+1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    distance = [0] * (n+1)
    
    queue = deque([1])
    distance[1] = 1
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == 0:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
                
    max_distance = max(distance)
    
    return distance.count(max_distance)