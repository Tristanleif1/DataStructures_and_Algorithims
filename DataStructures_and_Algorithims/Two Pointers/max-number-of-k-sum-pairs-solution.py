class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        sort = sorted(nums)
        l, r = 0, len(nums) - 1

        while l < r:
            if sort[l] + sort[r] == k:
                ans += 1
                l += 1
                r -= 1
            elif sort[l] + sort[r] < k:
                l += 1
            else:
                r -= 1

        return ans