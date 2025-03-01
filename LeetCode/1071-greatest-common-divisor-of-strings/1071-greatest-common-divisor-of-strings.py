class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        gcd_length = self.gcd(len(str1), len(str2))
        
        candidate = str1[:gcd_length]
        
        if str1 == candidate * (len(str1) // gcd_length) and str2 == candidate * (len(str2) // gcd_length):
            return candidate
        else:
            return ""
                


        