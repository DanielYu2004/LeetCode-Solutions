class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        
        check_list = []
        max_len = 0
        
        for i in s:
            if i in check_list:
                check_list = check_list[check_list.index(i)+1:]
            check_list.append(i)
            max_len = max(max_len, len(check_list))
        return(max_len)
