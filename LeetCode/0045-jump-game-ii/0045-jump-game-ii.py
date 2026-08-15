class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 마지막 인덱스까지 갈 수 있는 최소의 인덱스를 찾고, 그 인덱스까지 갈 수 있는 최소의 인덱스를 찾는다. 이걸 반복
        pivot = len(nums)-1 # index
        jumps = 0
        while pivot > 0:
            for i in range(pivot):
                if i + nums[i] >= pivot:
                    pivot = i
                    jumps += 1
                    break

        return jumps