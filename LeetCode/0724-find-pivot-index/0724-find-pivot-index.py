class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumLeft = []
        sumRight = []
        n = len(nums)
        for i in range(n):
            if i == 0: sumLeft.append(0)
            else: sumLeft.append(sum(nums[:i]))
        for j in range(n):
            if j == n-1: sumRight.append(0)
            else: sumRight.append(sum(nums[j+1:]))

        for k in range(n):
            if sumLeft[k]==sumRight[k]: return k
        return -1
        
        