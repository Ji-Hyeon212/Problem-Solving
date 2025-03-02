class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #차례대로 탐색하며 심을 수 있으면 심고, 아님 말고. 다 돌고 n 이 남으면 실패, 아니면 성공
        for pos in range(len(flowerbed)):
            left, right = pos-1, pos+1
            #(왼쪽 맨끝이거나 왼쪽이 0)이면서 (오른쪽이 0이면서 오른쪽 맨 끝)이면 해당 pos에 심는다. 
            if flowerbed[pos]==0 and (pos == 0 or flowerbed[left]==0) and (pos == len(flowerbed)-1 or flowerbed[right]==0):
                flowerbed[pos] = 1
                n -= 1
            if n <= 0:
                return True
        return False