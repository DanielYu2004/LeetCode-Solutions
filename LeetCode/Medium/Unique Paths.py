class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        steps = [[1 for x in range(n)] for x in range(m)]
        for i in range(1,m):
            for j in range(1,n):               
                steps[i][j] = steps[i-1][j] + steps[i][j-1] 
        return steps[-1][-1]   
