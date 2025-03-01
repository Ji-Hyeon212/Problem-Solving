class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)
        len2 = len(word2)
        word = ''
        
        if len1 > len2:
            for i in range(len2):
                word += word1[i]
                word += word2[i]
            word += word1[len2:]
        elif len1 < len2:
            for i in range(len1):
                word += word1[i]
                word += word2[i]
            word += word2[len1:]
        else:
            for i in range(len1):
                word += word1[i]
                word += word2[i]

        return word