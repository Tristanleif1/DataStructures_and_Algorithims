class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Iterative solution
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

    
    # # Backtracking algorithim approach
    #     res = []
    #     nums.sort()

    #     def backtrack(i, subset):
    #         if i == len(nums):
    #             res.append(subset[::])
    #             return

    #     # All subsets that include nums[i]
    #         subset.append(nums[i])
    #         backtrack(i + 1, subset)
    #         subset.pop()

    #     # All subsets that don't include nums[i]
    #     while i + 1 < len(nums) and nums[i] == nums[i + 1]:
    #         i += 1
    #             backtrack(i + 1, subset)
    # backtrack(0, [])
    # return res