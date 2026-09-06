import heapq

def solution(N, road, K):
    answer = 0
    
    # adjacent graph
    graph = [[] for _ in range(N+1)]
    for (a, b, cost) in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    # shortest path array
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    
    # (distance, # village)
    pq = [(0, 1)]
    
    # dijkstra
    while pq:
        cur_dist, cur = heapq.heappop(pq)
        
        if cur_dist > distance[cur]:
            continue
        
        for next_node, cost in graph[cur]:
            new_dist = cur_dist + cost
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
                
    answer = 0     
    for i in distance:
        if i <= K:
            answer += 1
    return answer