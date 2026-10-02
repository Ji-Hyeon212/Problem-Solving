def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2

        # mid분 동안 심사할 수 있는 총 인원
        people = 0

        for time in times:
            people += mid // time

            # 이미 n명 이상이면 더 계산할 필요 없음
            if people >= n:
                break

        # mid분이면 모든 사람 심사 가능
        if people >= n:
            answer = mid
            right = mid - 1

        # mid분으로는 부족
        else:
            left = mid + 1

    return answer