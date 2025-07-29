def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if (i + 1 > c):
            return i
    return len(citations)