class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       f = [0] + flowerbed + [0] # We are added zero's before and after array for comparison to see if we can place flower (an index needs zero's on either side for a flower to be able to be planted)

       for i in range(1, len(f) - 1): # skip first and last
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
       return n <= 0