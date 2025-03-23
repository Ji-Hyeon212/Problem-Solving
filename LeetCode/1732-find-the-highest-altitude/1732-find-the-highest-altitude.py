class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitudes = [0]
        now = 0
        for i in gain:
            now += i
            altitudes.append(now)
        return max(altitudes)