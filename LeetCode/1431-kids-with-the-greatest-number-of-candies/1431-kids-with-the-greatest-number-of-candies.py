class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = len(candies)
        boolean = [True for i in range(n)]
        for i in range(n):
            candies[i] += extraCandies
            if max(candies) == candies[i]: 
                boolean[i] = True
            else: 
                boolean[i] = False
            candies[i] -= extraCandies
        return boolean
        