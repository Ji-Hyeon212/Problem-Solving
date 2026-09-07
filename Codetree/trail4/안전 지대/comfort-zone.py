from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, k, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cur_x, cur_y = queue.popleft()

        for d in range(4):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny]:
                continue

            if grid[nx][ny] <= k:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))


max_height = 0
for i in range(n):
    for j in range(m):
        max_height = max(max_height, grid[i][j])

answer_k = 1
answer_zone = 0

for k in range(1, max_height + 1):
    visited = [[False] * m for _ in range(n)]
    zone_count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] > k and not visited[i][j]:
                bfs(i, j, k, visited)
                zone_count += 1

    if zone_count > answer_zone:
        answer_zone = zone_count
        answer_k = k

print(answer_k, answer_zone)