# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramDic = defaultdict(list)
        
        for word in strs:
            rearranged = ''.join(sorted(word))
            anagramDic[rearranged].append(word)

        return list(anagramDic.values())