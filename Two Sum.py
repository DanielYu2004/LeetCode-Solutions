class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        for i in range(len(nums)):
            test = target - nums[i]
            if test in check:
                return [check[test], i]
            else:
                check[nums[i]] = i
