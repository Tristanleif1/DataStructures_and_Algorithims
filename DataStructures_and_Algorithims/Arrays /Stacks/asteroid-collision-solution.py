class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #O(N) time and space complexity when using stack data structure
        ans = []

        for a in asteroids:
            # Start making asteroid collisons when there is asteroid in stack and current asteroid is negative
            # and asteroid on top of stack in positive guaranteeing a collision
            while ans and a < 0 and ans[-1] > 0:
                diff =  a + ans[-1]
                #if difference is negative, aseroid a wins and we remove smaller positive asteroid
                if diff < 0:
                    ans.pop()
                elif diff > 0:
                    #no asteroid in put can be zero so current asteroid will not be added to the stack,
                    #loop will also stop executing
                    a = 0
                else:
                    #asteroids are equal thus both will be destroyed
                    a = 0
                    ans.pop()
            # a must be positive or negative to be added to the stack
            if a:
                ans.append(a)
        return ans