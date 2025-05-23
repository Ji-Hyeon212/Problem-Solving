class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #중심 확장
        if not s: return None 
        start, end = 0, 0

        def expand_center(left, right):
            while left >= 0 and right <len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            #회문이 홀수 길이
            lo, ro = expand_center(i,i) 
            #회문이 짝수 길이
            le, re = expand_center(i, i+1)

            if ro - lo > end - start:
                start, end = lo, ro
            if re - le > end - start:
                start, end = le, re

        return s[start:end+1]


