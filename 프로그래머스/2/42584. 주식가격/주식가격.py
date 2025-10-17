def solution(prices):
    n = len(prices)
    stack = [] # stack에 인덱스를 넣어 저장
    counts = [0] * n
    
    for i, p in enumerate(prices):
        # 가격이 떨어지면
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop() # stack[-1]이 나옴
            counts[idx] = i - idx # 초 차이 저장
            
        stack.append(i)
        
    while stack:
        idx = stack.pop()
        counts[idx] = n - idx - 1
        
    return counts