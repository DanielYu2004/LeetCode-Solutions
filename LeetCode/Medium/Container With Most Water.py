class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        maxarea = 0
        for i in range(len(height)-1):
            for q in range(len(height)-1-i):
                #print(height[i], height[q+i+1],(q+1))
                #print(min(height[i], height[q+i+1]))
                mini = min(height[i], height[q+i+1])*(q+1)
                if mini > maxarea:
                    maxarea = mini
        return(maxarea)
                
        """
        x = 0
        y = len(height) - 1
        maxarea = 0
        while(x < y):
            if height[x] < height[y]:
                mini = height[x] * (y - x)
                if mini > maxarea:
                    maxarea = mini        
                x += 1
            else:
                mini = height[y] * (y - x)
                if mini > maxarea:
                    maxarea = mini
                y -= 1
        return maxarea
