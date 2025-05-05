from itertools import permutations

#소수 판별 num의 제곱근 범위 까지만 확인
def isPrime(num):
    if num <2: return False
    for i in range(2, int((num**0.5)+1)):
        if num % i == 0:
            return False
    return True

def solution(numbers):    
    answer = 0
    all_nums = set()
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            n = int(''.join(p))
            if isPrime(n) == True:
                all_nums.add(n)
    answer = len(all_nums)
    return answer