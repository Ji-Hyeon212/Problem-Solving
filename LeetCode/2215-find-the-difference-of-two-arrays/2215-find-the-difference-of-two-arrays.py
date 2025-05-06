class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set_nums1 = set(nums1)  #(1,2,3)
        set_nums2 = set(nums2)  #(1,2)
        list_nums1 = list(set_nums1)  #[1,2,3]
        list_nums2 = list(set_nums2)  #[1,2]

        for i in set_nums1:
            if i in set_nums2:    
                list_nums1.remove(i)    #[3]
        for i in set_nums2:
            if i in set_nums1:
                list_nums2.remove(i)    #[]
        answer = [list_nums1, list_nums2]
        return answer