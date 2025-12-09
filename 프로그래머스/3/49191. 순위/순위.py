def solution(n, results):
    # 가, 세 0~n까지 인접 행렬(행이 열을 이겼다.)
    # results돌면서 직접적인 승패 반영
    # 간접적인 승패 graph[i][k]==True고, graph[k][j]==True면 graph[i][j] = True
    # 승리 수(i 행에서 True 수) + 패배 수(i 열에서 True 수) == n-1이면 승패 확실
    
    graph = [[False] * (n+1) for _ in range(n+1)]
    
    for winner, looser in results:
        graph[winner][looser] = True
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
                
    answer = 0
    for i in range(1, n+1):
        won_cnt = 0
        lost_cnt = 0
        for j in range(1, n+1):
            if graph[i][j] == True:
                won_cnt += 1
        for j in range(1, n+1):
            if graph[j][i] == True:
                lost_cnt += 1
        
        if won_cnt + lost_cnt == n-1:
            answer += 1
            
    return answer