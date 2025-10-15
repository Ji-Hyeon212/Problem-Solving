from collections import defaultdict

def solution(clothes):
    selection = defaultdict(int)
    # 각 종류별 개수의 곱 - 1(아무 것도 안 입은 경우))
    for name, wear_type in clothes:
        selection[wear_type] += 1
        
    answer = 1
    # 해당 type의 옷을 하나씩 입거나 입지 않는 경우
    for count in selection.values():
        answer *= (count + 1)
        
    return answer - 1
        