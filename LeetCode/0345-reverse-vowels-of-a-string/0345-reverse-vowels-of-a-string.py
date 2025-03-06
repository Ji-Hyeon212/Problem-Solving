class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        store = []
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                store.append(s_list[i])
        numOfVowels = len(store)
        count = 0
        for j in range(len(s_list)):
            if s_list[j] in vowels:
                s_list[j] = store[numOfVowels-count-1]
                count += 1
        return ''.join(s_list)

        