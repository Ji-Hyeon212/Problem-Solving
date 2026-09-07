from collections import deque

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

villages = []

for y in range(n):
    for x in range(n):

        if grid[y][x] == 1 and not visited[y][x]:
            q = deque()
            q.append((y, x))
            visited[y][x] = True

            count = 1

            while q:
                cy, cx = q.popleft()

                for i in range(4):
                    ny = cy + dy[i]
                    nx = cx + dx[i]

                    if 0 <= ny < n and 0 <= nx < n:
                        if grid[ny][nx] == 1 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((ny, nx))
                            count += 1

            villages.append(count)

villages.sort()

print(len(villages))
for count in villages:
    print(count)