class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = []
       
        for i in range(numRows):
            arr.append([])
        level = 0
        down = True
        final = ""
        for i in s:
            if numRows == 1:
                return(s)
            #print("level" , level, "char", i)
            #print(arr[level])
            #print(arr[1])
            #print(arr[2])
            #print(level)
            #print(i)
            arr[level].append(i)
            
            if level == numRows-1:
                down = False
                
            if level == 0:
                down = True
                
            if down == True: 
                level +=1
            if down == False:
                level -=1
                
        for i in range(numRows):
            for q in (arr[i]):
                final += q
            print(arr[i])
                


        return(final)
