class Solution(object):
    def specialGrid(self, N):
        """
        :type N: int
        :rtype: List[List[int]]
        """
        if N == 0:
            return [[0]]
    
        size = 2**N
        half = size // 2
        offset = 4**(N-1)
        grid = [[0] * size for _ in range(size)]
        quater_grid = self.specialGrid(N-1)
        
        for i in range(half):
            for j in range(half):
                grid[i][j] = quater_grid[i][j] + 3*offset
                grid[i][j+half] = quater_grid[i][j] + 0*offset
                grid[i+half][j] = quater_grid[i][j] + 2*offset
                grid[i+half][j+half] = quater_grid[i][j] + 1*offset
                
        return grid