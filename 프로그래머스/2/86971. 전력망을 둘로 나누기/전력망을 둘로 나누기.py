from collections import deque, defaultdict

def solution(n, wires):
    graph = defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(start, blocked):
        visited = set([start])
        queue = deque([start])
        count = 1
        
        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                if (node, next_node) == blocked or (next_node, node) == blocked:
                    continue
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
                    count += 1
        return count
    
    min_diff = n
    for a, b in wires:
        count_a = bfs(a, (a, b))
        diff = abs(n - 2 * count_a)
        min_diff = min(min_diff, diff)
        
    return min_diff