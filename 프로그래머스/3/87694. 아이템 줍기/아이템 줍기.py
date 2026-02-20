from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    rectangle = [[e*2 for e in rect] for rect in rectangle]
    characterX *=2
    characterY *=2
    itemX *= 2
    itemY *= 2
    
    board = [[0]*102 for _ in range(102)]
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                board[x][y] = 1
                
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                board[x][y] = 0
                
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*102 for _ in range(102)]
    visited[characterX][characterY] = True
# 캐릭터의 위치 배열
    queue = deque([(characterX, characterY, 0)])
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == itemX and y == itemY:
            return dist //2
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0<=nx<102 and 0<=ny<102:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))