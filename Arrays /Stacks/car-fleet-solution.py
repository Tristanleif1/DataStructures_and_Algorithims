class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #Create an array of pairs using the zip function
        pair = [[p, s] for p, s in zip(position, speed)]
        #Sort the array of pairs in reverse sorted order
        stack = [] #Will tell us how many car fleets we will have at the end
        for p, s in sorted(pair)[::-1]:
            #We can find out the time at which a car will reach the destination via the decimal division below
            #Decimal division
            stack.append((target - p) / s)
            #Once we append a time to our stack we want to determine if it overlaps with another car (time) in a stack
            #If stack has just one car, we dont need to do anything. If there are at least 2, a collision is possible
            #If the time of the car at the top of the stack reachest the destination before the car ahead of it at index 2,
            #This means they collide and we must pop from the top of the stack and decrease the number of car fleets. 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
