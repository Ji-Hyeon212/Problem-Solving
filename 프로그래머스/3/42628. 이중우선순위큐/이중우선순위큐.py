import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    valid_counts = {}
    for op in operations:
        opcode, num_str = op.split() # 문자열 split 한 결과도 문자열
        num = int(num_str)
        
        if opcode == 'I':
            heapq.heappush(min_heap, num) # heapq 사용 문법 check
            heapq.heappush(max_heap, -num)
            valid_counts[num] = valid_counts.get(num, 0) + 1
        elif opcode == 'D':
            if sum(valid_counts.values()) == 0:
                continue;
            if num == 1:
                while max_heap:
                    max_val = -heapq.heappop(max_heap)
                    if valid_counts.get(max_val, 0) > 0:
                        valid_counts[max_val] -= 1
                        break
            else:
                while min_heap:
                    min_val = heapq.heappop(min_heap)
                    if valid_counts.get(min_val, 0) > 0:
                        valid_counts[min_val] -= 1
                        break
                        
    valids = sum(valid_counts.values())
    if valids == 0:
        return [0, 0]
    else:
        while max_heap:
            max_val = -heapq.heappop(max_heap)
            if valid_counts.get(max_val, 0) > 0:
                break
        while min_heap:
            min_val = heapq.heappop(min_heap)
            if valid_counts.get(min_val, 0) > 0:
                break
                
        return [max_val, min_val]
    