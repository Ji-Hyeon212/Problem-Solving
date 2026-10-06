n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.\
# 가중치 기준 오름차순 정렬
edges.sort(key=lambda x: x[2])

parent = [i for i in range(n + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA


answer = 0
cnt = 0

for a, b, cost in edges:

    # 서로 다른 집합이면
    if find(a) != find(b):
        union(a, b)

        answer += cost
        cnt += 1

        # MST는 간선 N-1개
        if cnt == n - 1:
            break

print(answer)