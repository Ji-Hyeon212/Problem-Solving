def solution(sizes):
    answer = 0
    rotated = []
    for w, h in sizes:
        if w < h:
            w, h = h, w
        rotated.append([w, h])
    cols = list(zip(*rotated))
    max_w = max(cols[0])
    max_h = max(cols[1])
    
    answer = max_w * max_h
    
    return answer