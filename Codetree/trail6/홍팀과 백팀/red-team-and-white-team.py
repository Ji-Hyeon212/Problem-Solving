from collections import deque

n, m = map(int, input().split()) # 사람 수, 대결 횟수
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph= [[] for _ in range(n+1)]
for edge in edges:
    a, b = edge
    graph[a].append(b)
    graph[b].append(a)

color = [0] * (n+1)

def bfs(x):
    color[x] = 1
    q = deque([x])
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            # 색이 0이면 반대색 지정
            if color[next] == 0:
                color[next] = -color[cur]
                q.append(next)
            # 색이 같으면 모순
            elif (color[next] == color[cur]):
                return False
    return True
    
for i in range(1, n+1):
    if (color[i] == 0):
        if not bfs(i):
            print(0)
            break

else:
    print(1)

    
    


    