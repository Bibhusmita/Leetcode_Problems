class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        beg , end = 0, len(nums) - 1
        while beg <= end:
            mid = (beg + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                beg = mid + 1
            else:
                end = mid - 1
        if target > nums[mid]:
            return mid + 1
        else:
            return mid
        
        