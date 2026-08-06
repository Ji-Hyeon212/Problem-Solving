class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = 0
        
        for i in range(len(nums)):
            if i > reachable:
                return False

            reachable = max(reachable, i + nums[i])

            if reachable >= len(nums) - 1:
                return True

        return True

        