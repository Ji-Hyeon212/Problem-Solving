n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
best = 0
# Please write your code here.
# 일자 블록 (가로)
if m >=3:
    for r in range(n):
        for c in range(m-2):
            s = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            best = max(best, s)
# 일바 블록 (세로)
if (n >= 3):
    for c in range(m):
        for r in range(n-2):
            s = grid[r][c] + grid[r+1][c] + grid[r+2][c]
            best = max(best, s)
# L자
if n >= 2 and m >= 2:
    for r in range(n - 1):
        for c in range(m - 1):
            vals = [grid[r][c], grid[r][c+1], grid[r+1][c], grid[r+1][c+1]]
            s = sum(vals) - min(vals)
            best = max(best, s)

print(best)