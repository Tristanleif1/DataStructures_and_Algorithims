class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        #[0, -5, 1, 5, 0, -7]

        #[]

        #To find the highest altitude, we need to calculate the cumulative sum of the altitude gains
        #at each step. Starting from the initial altitude of 0, we keep adding the gain at each step to 
        #the current altitude. The highest altitude reached during this process is the answer
        # we are looking for

        maxAltitude = 0
        currentAltitude = 0

        for height in gain:
            currentAltitude += height
            if currentAltitude > maxAltitude:
                maxAltitude = currentAltitude

        return maxAltitude
