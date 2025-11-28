def solution(video_len, pos, op_start, op_end, commands):
    # - mm:ss 시간을 초 단위로 변환한다.(video_len, pos, op_start, op_end)
    # - commands를 순회하며 prev는 pos-10, next는 pos+10
    #     - pos가 op_start<=pos<=op_end인 경우 op_end로 이동
    #     - pos가 0 > pos 면 0으로 이동, video_len < pos면 video_len으로 이동
    # - pos를 mm:ss 형식으로 return
    
    def calc(time):
        min, sec = map(int, time.split(":"))
        total = min * 60 + sec
        return total
    
    def reverse_calc(time):
        min = time // 60
        sec = time % 60
        return f"{min:02d}:{sec:02d}"
        
    def calc_all(video_len, pos, op_start, op_end):
        return calc(video_len), calc(pos), calc(op_start), calc(op_end)
    
    s_video_len, s_pos, s_op_start, s_op_end = calc_all(video_len, pos, op_start, op_end)
    
    for command in commands:
        if s_op_start <= s_pos <= s_op_end:
            s_pos = s_op_end
            
        if command == 'prev':
            s_pos -= 10
            if s_pos < 0:
                s_pos = 0
            
        elif command == 'next':
            s_pos += 10
            if s_pos > s_video_len:
                s_pos = s_video_len
                
        if s_op_start <= s_pos <= s_op_end:
            s_pos = s_op_end
        
    return reverse_calc(s_pos)
        
    