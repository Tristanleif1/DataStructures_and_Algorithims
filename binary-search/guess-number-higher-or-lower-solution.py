class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:  # Use <= instead of < to include the upper bound in the search
            mid = (lo + hi) // 2  # Use integer division to avoid floating-point values
            res = guess(mid)
            if res == 0:
                return mid  # Correct guess, return the number
            elif res == 1:
                lo = mid + 1  # The picked number is higher, adjust the lower bound
            else:
                hi = mid - 1  # The picked number is lower, adjust the upper bound
        return lo