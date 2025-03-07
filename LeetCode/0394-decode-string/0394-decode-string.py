class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        target = ''
        num = 0

        for i in s:
            if i.isalpha():
                target += i
            elif i.isdigit():
                num = num*10 + int(i)
            elif i == '[':
                stack.append((target, num))
                num = 0
                target = ''
            elif i == ']':
                last_word, tmp_num = stack.pop()
                target = last_word + target * tmp_num

        return target
            

        