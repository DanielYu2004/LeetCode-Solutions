class Solution(object):
    def climbStairs(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return(n)
        
        first = 1
        second = 2
        start = 1
        sol = 0

        while start < (n - 1):
            sol = first + second
            first = second
            second = sol
            start = start + 1
        return(sol)
