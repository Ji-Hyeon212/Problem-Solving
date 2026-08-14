def solution(n):
    snail = [[0]* (i+1) for i in range(n)]
    
    row = -1
    col = 0
    num = 1
    # direction 3방향 아래(0), 오른쪽(1), 좌상향(2)
    for direction in range(n):
        for j in range(n-direction):
            if (direction % 3) == 0:
                row += 1
            elif (direction % 3) == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            snail[row][col] = num
            num += 1
    answer = []
    for row in snail:
        answer.extend(row)
                
    return answer
        
    