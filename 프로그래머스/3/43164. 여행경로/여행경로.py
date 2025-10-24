from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for depart, dest in tickets:
        routes[depart].append(dest)
        
    for depart in routes:
        routes[depart].sort()
        
    result = [] # 경로 결과
    def dfs(current_airport, path):
        nonlocal result
        
        if len(path) == len(tickets) + 1:
            result = path
            return True
        
        destinations = routes[current_airport]
        for i in range(len(destinations)):
            next_airport = destinations.pop(i)
            if dfs(next_airport, path + [next_airport]):
                return True
            destinations.insert(i, next_airport)
        return False
    
    dfs("ICN", ["ICN"])
    
    return result
                