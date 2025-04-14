from bisect import bisect_left
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            min_potion = (success + spell -1) // spell
            idx = bisect_left(potions, min_potion)
            result.append(m-idx)

        return result