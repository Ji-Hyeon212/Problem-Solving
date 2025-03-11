from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
    
        freq = Counter(arr)
        occurrences = list(freq.values())
        
        return len(occurrences) == len(set(occurrences))