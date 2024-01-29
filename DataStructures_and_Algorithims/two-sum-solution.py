class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = defaultdict()

        for i, num in enumerate(nums):
            difference = target - num
            if difference in twoSum:
                return [twoSum[difference], i]
            twoSum[num] = i
