class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [0 for i in range(n)]
        answer = 0

        def dfs(i):
            visited[i]=1
            for j in range(n): 
                if isConnected[i][j] and not visited[j]:
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                answer += 1
        return answer