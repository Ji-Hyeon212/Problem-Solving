from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    global max_count 
    max_count = 0

    def backtrack(current_k, count):
        global max_count
        max_count = max(max_count, count)
        
        if count == n:
            return
        
        for i in range(n):
            min_fatigue, cost = dungeons[i]
            # 아직 방문 전이고 현재 피로도가 최소 피로도 이상인 경우 전진
            if not visited[i] and current_k >= min_fatigue:
                visited[i] = True
                backtrack(current_k - cost, count + 1)
                visited[i] = False
        
    backtrack(k, 0)
    
    return max_count