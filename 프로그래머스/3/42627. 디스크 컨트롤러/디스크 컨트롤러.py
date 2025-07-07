import heapq

def solution(jobs):
    jobs.sort() #요청 시간 순으로 정렬
    n = len(jobs)
    time, idx, total = 0, 0, 0
    heap = []
    while idx < n or heap:
        #대기 큐에 소요 시간이 짧은 순서대로 담음
        while idx < n and jobs[idx][0] <= time:
            request_time, duration = jobs[idx]
            heapq.heappush(heap, (duration, request_time))
            idx += 1

        if heap: #소요시간이 작은 순서대로 실행
            duration, request_time = heapq.heappop(heap)
            time += duration
            total += time - request_time
        else:
            time = jobs[idx][0]

    return total // n