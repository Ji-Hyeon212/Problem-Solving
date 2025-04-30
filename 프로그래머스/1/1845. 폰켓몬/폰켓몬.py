from itertools import combinations
def solution(nums):
    answer = 0
    type = len(set(nums))
    N = len(nums)
    if N//2 <= type:
        answer = N//2
    else:
        answer = type
    return answer