n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 종료시간 순 정렬
meetings.sort(key=lambda x: x[1])

# 초깃값 지정
cnt = 0
end_time = -1
for start, end in meetings:
    # 이전 종료 시점보다 시작 시간이 이후이면 카운트하고 종료시각 갱신
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)
    