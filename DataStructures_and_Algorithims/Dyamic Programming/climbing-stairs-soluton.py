class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 
        #Intialize 'one' and 'two' to 1. These variables act as caches for the number of ways to reach the current step 'one' and the previous step 'two'

        for i in range(n - 1):
            tmp = one # 'tmp' temporarily stores the current number of ways to reach the current step before updating 'one'. This is necessary because the value of 'one' is needed to update 'two'.
            one = one + two # Update 'one' to the sum of 'one' and 'two'. This reflects the Fibonacci relation: F(n) = F(n-1) + F(n-2), where 'one' corresponds to F(n) and 'two' corresponds to F(n-1) after each iteration.
            two = tmp # Update 'two' to the previous value of 'one'. This shifts the window one step forward, preparing for the next iteration.

        return one