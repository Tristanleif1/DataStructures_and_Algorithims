class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniqueSet = set()

        for num in nums:
            if num not in uniqueSet:
                uniqueSet.add(num)
            else:
                return True
        return False