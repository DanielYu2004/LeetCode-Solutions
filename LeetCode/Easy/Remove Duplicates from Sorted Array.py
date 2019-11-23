class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(len(nums)-1):
            if nums[j] != nums[j+1]:
                i += 1
                nums[i] = nums[j+1]
        
        return (i+1)
