class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum = 0
        containter = 0
        left = 0
        right = len(height)-1
        while(left < right):
            containter = (right-left) * min(height[left], height[right])
            maximum = max(maximum, containter)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maximum