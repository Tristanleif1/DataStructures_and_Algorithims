class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding Window 
        #O(N) time complexity
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            #A while loop should be used to ensure that characters are removed from the start of the window
            #and advances l until the character s[r] is not in 'charSet'. This ensures that all duplicates
            #of s[r] are removed from the current window.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet))
        return res
