class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1): return s
        zigzag= [""] * numRows
        direction = 1
        row = 0

        for i, ch in enumerate(s):
            zigzag[row] += ch
            row += direction
            if (row == 0 or row == numRows-1):
                direction = -direction
        result = ''.join(zigzag)       
        return result