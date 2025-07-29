def solution(name):
    n = len(name)
    answer = 0
    word_count = 0
    cursor_count = 0
    min_count = n - 1

    for i in name:
        word_count += min(ord(i)-ord('A'), ord('Z')-ord(i)+1)
    
    for i in range(n):
        next_id = i + 1
        while next_id < n and name[next_id] == 'A':
            next_id += 1
        cursor_count = min((i*2+n-next_id), (i+2*(n-next_id)))
        min_count = min(min_count, cursor_count)
    answer = word_count + min_count
    return answer