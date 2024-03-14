class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryRep = bin(n)

        count = 0
        for x in binaryRep:
            if x == "1":
                count += 1
        return count
       