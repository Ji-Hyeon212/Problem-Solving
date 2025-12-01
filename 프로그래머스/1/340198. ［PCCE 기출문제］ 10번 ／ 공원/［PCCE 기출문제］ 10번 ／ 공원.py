def can_place_mat(park, mat):
    # 깔 수 있는 좌상단 범위를 구한다.
    R = len(park)
    C = len(park[0])
    
    max_r = R - mat
    max_c = C - mat
    #돗자리가 공원보다 크면 False
    if max_r < 0 or max_c < 0: 
        return False
    # 좌상단 범위를 순회
    for r in range(max_r+1):
        for c in range(max_c+1):
            # 돗자리를 폈을 때 -1이 아닌 게 있으면 dirtybit 업뎃하고 다음 좌상단
            isClear = True
            for i in range(mat): # 행
                if isClear == False:
                    break
                    
                for j in range(mat): # 열
                    if (park[r + i][c + j] != "-1"):
                        isClear = False
                        break
            if isClear:
                        return True
    return False
    
def solution(mats, park):
    # 매트 종류는 최대 10가지, 매트 크기는 20 이하
    # 공원의 가, 세 파악. 길이가 0이면 -1 리턴
    # 매트 내림 차순 정렬. 매트 순회하며 공원에 들어가는 지 확인
    # 가능한 모든 좌상단을 돌며 매트 범위 안에 사람이 있는지 확인
    sorted_mats = sorted(mats, reverse = True)
    
    for mat in sorted_mats:
        if can_place_mat(park, mat):
            return mat # 내림차순했으므로, 첫번째 통과한 매트가 가장 큰 돗자리
    
    return -1
    