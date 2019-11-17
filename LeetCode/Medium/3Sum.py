class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twosum(self, arr, target):
            """
            check = {}
            for i in range(len(arr)):
                test = target - arr[i]
                if test in check:
                    print(target, check[test], i)
                    return [check[test], i]
                else:
                    check[arr[i]] = i
            """
            """
            indexes = []
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    if arr[i] + arr[j] == target:
                        indexes.append([i, j])
            return(indexes)
            """
            pairs = []
            hmap = dict()
            for i in range(len(arr)):
                key = target - arr[i]
                if key in hmap:
                    pairs.append([arr[i], arr[hmap[key]]])
                hmap[arr[i]] = i
            return(pairs)        
        
        
        targetsum = 0
        sollist = []
        numlen = len(nums)
        if numlen < 3:
            return(sollist)
        else:
            for i in range(numlen):
                targetsum -= nums[i]
                #print("inverse",nums[i+1:])
                #print("target", targetsum)
                index = twosum(self, nums[i+1:],targetsum)
                #print(index)
                if index:
                    for q in (index):
                        #print(q)
                        #arr = (nums[i], (nums[i+1:])[q[0]], (nums[i+1:])[q[1]])
                        arr = (nums[i], q[0],q[1])
                        #print(arr)
                        """
                        for r in range(len(sollist)):
                            if sorted(sollist[r]) == sorted(arr):
                                print((sollist[r]) , sorted(arr))
                                unique = False
                        """
                        arr = sorted(arr)
                        if not arr in sollist:
                            sollist.append(arr)

                targetsum = 0
            return(sollist)
        
