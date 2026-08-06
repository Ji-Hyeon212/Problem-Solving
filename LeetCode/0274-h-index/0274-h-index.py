class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h_index = 0
        for i, citation in enumerate(citations):
            cnt = i + 1
            if (citation >= cnt):
                h_index = cnt
            else: break
        return h_index
        