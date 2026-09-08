n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
visited[0] = True

answer = float('inf')

def dfs(depth, cur, total):
    global answer

    if total >= answer:
        return

    if depth == n:
        if A[cur][0] != 0:
            answer = min(answer, total + A[cur][0])
        return

    for next_city in range(n):
        if visited[next_city]:
            continue

        if A[cur][next_city] == 0:
            continue

        visited[next_city] = True
        dfs(depth + 1, next_city, total + A[cur][next_city])
        visited[next_city] = False

dfs(1, 0, 0)
print(answer)