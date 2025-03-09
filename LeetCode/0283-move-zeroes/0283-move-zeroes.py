class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dict = {}
        for i in nums:
            if i in dict: dict[i] += 1
            else: dict[i] = 1
        if 0 in dict: 
            zero_count = dict[0]
            for i in range(zero_count):
                nums.remove(0)
                nums.append(0)


        