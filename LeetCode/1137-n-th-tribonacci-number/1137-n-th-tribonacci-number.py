class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {0: 0, 1: 1, 2: 1}
        def memoization(a):
            if a in memo:
                return memo[a]
            memo[a] = memoization(a-3) + memoization(a-2) + memoization(a-1)
            return memo[a]
            
        return memoization(n)