class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_str = list(str(n))
        numbers = map(int, num_str)
        print(numbers)
        M = max(numbers)
        numbers.remove(M)
        M_2nd = max(numbers)
        
        ans = M * M_2nd
        
        return ans