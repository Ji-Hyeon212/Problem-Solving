from collections import deque

perfumes = [] # 향료

# 작업 처리
def work(command):
    if command[0] == 1:
        init(command)
    elif command[0] == 2:
        add(command)
    elif command[0] == 3:
        remove(command)
    elif command[0] == 4:
        blend(command)
    elif command[0] == 5:
        combine(command)
    
# 향료 준비 N종, 1번, 2번...
def init(command):
    N = command[1]
    # 향도
    global perfumes
    perfumes = [0] + command[2:]
# 향료 추가
def add(command):
    global perfumes
    perfumes.append(command[1])

# 향료 폐기
def remove (command):
    idx = command[1]

    if idx <= 0 or idx >= len(perfumes):
        print(-1)
        return

    if perfumes[idx] == -1:
        print(-1)
        return

    print(perfumes[idx])
    perfumes[idx] = -1
    
# 유효한 항수 리스트
def get_scent_list():
    result = []
    for i  in range(1, len(perfumes)):
        if perfumes[i] != -1:
            result.append(perfumes[i])
    return result

def two_pointer(scents, need):
    n = len(scents)
    left = 0
    right = n-1
    count = 0

    while left < n:
        while right >= 0 and scents[left] + scents[right] >= need:
            right -= 1

        count += n - (right + 1)
        left += 1

    return count

# 블렌딩
def blend(command):
    K = command[1]
    scents = get_scent_list()
    visited = [False] * (K + 1)
    q = deque()

    q.append((0, 0))
    visited[0] = True

    while q:
        total, count = q.popleft()
        for scent in scents:
            next_total = total + scent

            if next_total > K:
                continue

            if visited[next_total]:
                continue
            
            if next_total == K:
                print(count + 1)
                return
            
            visited[next_total] = True
            q.append((next_total, count + 1))
    print(-1)

# 향수 구성
def combine(command):
    K = command[1]

    scents = get_scent_list()
    scents.sort()

    answer = 0

    for top in scents:
        need = K - top
        answer += two_pointer(scents, need)
    print(answer)

Q = int(input())
for _ in range(Q):
    command = list(map(int, input().split()))
    work(command)
