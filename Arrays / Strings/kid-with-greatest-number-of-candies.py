class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        return [candy + extraCandies >= M for candy in candies]

        #Multiple kids can have the greatest number of candies because as we iterate through the array of candies each kid has, we are giving each kid extra candies and comparing the new number of candies each kid has compared to the max num of candies of the original list before the kids were each given extra candies.




        #OR
        maxCandies = max(candies)
        result = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result