class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        twoSumChecker = {}

        for i, num in enumerate(numbers, start=1):
            sumNeeded = target - num
            if sumNeeded in twoSumChecker:
                return [twoSumChecker[sumNeeded], i]
            twoSumChecker[num] = i