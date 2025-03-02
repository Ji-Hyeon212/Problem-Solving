def solution(numbers):
    answer = ''
    temp = []
    for num in numbers:
        temp.append(str(num))
    temp.sort(key=lambda x:x*3, reverse=True)
    answer = ''.join(temp)
    if int(answer)==0:
        answer = '0'
    return answer