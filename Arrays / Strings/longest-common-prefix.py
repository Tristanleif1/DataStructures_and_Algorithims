class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        #We're iterating through every character in the first word
        for i in range(len(strs[0])):
            #Iterate through all of the strings 
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res