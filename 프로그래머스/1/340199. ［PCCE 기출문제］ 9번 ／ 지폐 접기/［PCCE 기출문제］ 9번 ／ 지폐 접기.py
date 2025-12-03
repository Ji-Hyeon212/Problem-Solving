def solution(wallet, bill):
    answer = 0
    
    while (min(map(int, bill)) > min(map(int, wallet))) or (max(map(int, bill)) > max(map(int, wallet))):
           # 긴 쪽을 반으로 접는다.
        if (bill[0] > bill[1]):
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] //2
        answer += 1
        
    return answer