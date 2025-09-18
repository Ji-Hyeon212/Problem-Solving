def solution(brown, yellow):
    total = brown + yellow
    # 가로 또는 세로는 total의 root 값까지 계산
    for height in range(1, int(total ** 0.5) + 1):
        if (total%height == 0):
            width = total // height
            yello_width = width - 2
            yello_height = height - 2
            # y_w와 y_h 곱이 넓이와 같으면
            if (yello_width * yello_height == yellow):
                return [width, height]
    
    
