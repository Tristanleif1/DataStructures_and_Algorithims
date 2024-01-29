class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = defaultdict()
        #O(N) time complexity since hashtable lookups take consant time on average
        for i, num in enumerate(nums):
            difference = target - num
            if difference in twoSum:
                return [twoSum[difference], i]
            twoSum[num] = i

#OR Brute Force approach O(n^2) time complexity because we run 2 for loops, not as efficient as a hash map
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []