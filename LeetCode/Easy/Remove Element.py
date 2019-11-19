class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = nums.count(val)
        for i in range(count):
            nums.remove(val)
        
        return(len(nums))
        
