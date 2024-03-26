class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        sorted_stones = sorted(stones)

        while len(sorted_stones) > 1:
            y = sorted_stones.pop()
            x = sorted_stones.pop()

            #If stones are equal, no additional if statement is needed, popping both stones will take care of this case, we only need to add
            # an if conditional if their weights differ.

            if x != y:
                new_stone = y - x
                sorted_stones.append(new_stone)
                #After appending the new stone you need to sort the list again to ensure the stones are in correct ascending order by weight
                sorted_stones.sort()
        #Return the last remaining stone if there are no stones return 0
        return sorted_stones[0] if sorted_stones else 0