import math
def solution(progresses, speeds):
    days = []
    release = []
    numOfWork = []
    for i in range(len(progresses)):
        day = math.ceil((100-progresses[i])/speeds[i])
        days.append(day)
    for j in days:
        if len(release)==0:
            release.append(j)
        else:
            if j <= release[0]:
                release.append(j)
            else:
                numOfWork.append(len(release))
                release.clear()
                release.append(j)
    numOfWork.append(len(release))
    return numOfWork