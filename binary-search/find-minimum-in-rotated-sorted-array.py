class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            #If array is not sorted, we perform our binary search
            m = (left + right) // 2
            res = min(res, nums[m])
            #Is mid value apart of left sorted portion, if it is --> we want to search the right sorted portion
            if nums[m] >= nums[left]:
                left = m + 1
            #IF we are in right sorted portion, we want to search the left sorted portion.
            else:
                right = m - 1
        return res