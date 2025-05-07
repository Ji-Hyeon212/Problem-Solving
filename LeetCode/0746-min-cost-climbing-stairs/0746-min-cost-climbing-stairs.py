class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0]*n

        #dp 테이블에는 ai 번째 계단을 오를 때까지의 최소 값을 저장
        #i-1번째와 i-2번째 + i 의 값 중 더 작은 값을 구하면 됨.
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        print(dp)
        # 마지막 계단을 넘어가기 위한 최소 비용 반환
        return min(dp[n-1], dp[n-2])
        