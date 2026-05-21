def solution(participant, completion):
    hash_map = {}

    # 참가자 수 세기
    for name in participant:
        if name in hash_map:
            hash_map[name] += 1
        else:
            hash_map[name] = 1

    # 완주자 수 빼기
    for name in completion:
        hash_map[name] -= 1

    # 값이 1 남은 사람이 완주 못한 사람
    for name in hash_map:
        if hash_map[name] > 0:
            return name