n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [1, -1, -1, 1] # 1, 2, 3, 4방향
dy = [-1, -1, 1, 1]

answer = 0

for r in range(2, n): # 행
    for c in range(1, n-1): # 열
        for a in range(1, n): # 1번 방향 한변 길이
            for b in range(1, n): # 2번 방향 한변 길이
                # 격자에서 대각선크기 = 가로 크기 = 세로 크기
                # 맨 왼쪽 4번 꼭짓점
                if c-b < 0:
                    continue;
                # 맨 오른쪽 2번 꼭짓점 
                if c+a >= n:
                    continue;
                # 맨 위 3번 꼭짓점
                if r-a-b < 0:
                    continue;

                cur_r, cur_c = r, c 
                total = 0

                for _ in range(a):
                    total += grid[cur_r][cur_c]
                    cur_r -= 1
                    cur_c += 1
                for _ in range(b):
                    total += grid[cur_r][cur_c]
                    cur_r -= 1
                    cur_c -= 1
                for _ in range(a):
                    total += grid[cur_r][cur_c]
                    cur_r += 1
                    cur_c -= 1
                for _ in range(b):
                    total += grid[cur_r][cur_c]
                    cur_r += 1
                    cur_c += 1
                
                answer = max(answer, total)

print(answer)