class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            minlen = len(min(strs, key=len))
        else:
            return("")
        prefix = ""
        for i in range(minlen):
            check = strs[0][i]
            for r in range(len(strs)):
                if strs[r][i] != check:
                    return(prefix)
            prefix = prefix + check
        return(prefix)
                    
        
