def solution(k, room_number):
    rooms = {}
    answer = []
    
    def find(room):
        path = []
        
        while room in rooms:
            path.append(room)
            room = rooms[room]
            
        for r in path:
            rooms[r] = room
        
        return room
    
    for num in room_number:
        empty_room = find(num) # 고객이 원한 방 번호의 대표 번호
        answer.append(empty_room)
        rooms[empty_room] = empty_room + 1
    
    return answer