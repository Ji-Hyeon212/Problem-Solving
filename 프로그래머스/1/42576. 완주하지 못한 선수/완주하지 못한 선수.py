def solution(participant, completion):
    runners = {}
    for part in participant:
        if part in runners:
            runners[part] += 1
        else:
            runners[part] = 1
            
    for complete in completion:
        runners[complete] -= 1

    for runner in runners:
        if runners[runner] != 0:
            return runner
    