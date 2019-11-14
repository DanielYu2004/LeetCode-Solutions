class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sorted_list = sorted(nums1 + nums2)
        length = len(sorted_list)
        print(sorted_list)
        if length % 2 == 0:
            return((sorted_list[length/2] + sorted_list[(length/2)-1])/float(2))
        else: 
            return(sorted_list[length//2])            
