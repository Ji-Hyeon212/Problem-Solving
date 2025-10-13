from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    max_count = 0
    for dungeon_seq in permutations(dungeons, n):
        current_k = k
        count = 0
        for min_fatigue, cost in dungeon_seq:
            # 현재 피로도가 최소 피로도 이상이면 탐험(피로도 차감)
            if current_k >= min_fatigue:
                current_k -= cost
                count += 1
            else:
                break
        #최대 던전 수 갱신
        max_count = max(max_count, count)
        
        if max_count == n:
            return n
    
    return max_count