class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in d:
                return [d[comp], i]               
            else:                
                d[num] = i

s = Solution()
print(s.twoSum([2,7,11,17],9))