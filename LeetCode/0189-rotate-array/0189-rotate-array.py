class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # k가 n보다 큰 경우

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 전체 뒤집기
        reverse(0, n - 1)
        # 처음 k개
        reverse(0, k - 1)
        # 나머지 n-k개
        reverse(k, n - 1)