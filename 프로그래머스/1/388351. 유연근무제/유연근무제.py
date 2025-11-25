def solution(schedules, timelogs, startday):
    # schedules 직원들이 설정한 출근 희망 시각 배열
    # timelogs 직원들이 일주일 동안 출근한 시각 2차원 배열
    # startday 이벤트를 시작한 요일 1~7(월~일)
    # return 상품을 받을 직원의 수
    # 주말은 이벤트 제외니까 시작한 날에 맞게 주말은 배제해야함.
    weekdays = {
        1: [1, 2, 3, 4, 5],
        2: [1, 2, 3, 4, 7],
        3: [1, 2, 3, 6, 7],
        4: [1, 2, 5, 6, 7],
        5: [1, 4, 5, 6, 7],
        6: [3, 4, 5, 6, 7],
        7: [2, 3, 4, 5, 6],
    }
    def isOnTime(schedule, time):
        sch_hour = schedule // 100
        sch_min = schedule % 100
        time_hour = time // 100
        time_min = time % 100
        
        sch_total = (sch_hour * 60) + sch_min
        time_total = (time_hour * 60) + time_min

        return time_total - sch_total <=10
    
    no_gift = 0
    
    for i, timelog in enumerate(timelogs):
        for item in weekdays[startday]:
            if isOnTime(schedules[i], timelog[item-1]) == False:
                no_gift += 1
                break

    return len(schedules) - no_gift
            