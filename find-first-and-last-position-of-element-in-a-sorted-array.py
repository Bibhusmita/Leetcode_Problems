class Solution:
    def indexValue(self, nums, target, flag):
        beg, end = 0, len(nums) - 1
        idx = -1
        while beg <= end:
            mid = (beg + end)//2
            if nums[mid] == target:
                idx = mid
                if flag:
                    end = mid - 1
                else:
                    beg = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                beg = mid + 1 
        return idx

    
    def searchRange(self, nums, target):
        return [self.indexValue(nums, target, True ), self.indexValue(nums, target, False)]
        
    
s = Solution()
print(s.searchRange([5,7,7,8,8,11],8))