class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans


# Monotonic decreasing stack #O(N) Time Complexity

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Monotonic decreasing stack
        numOfDays = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prevI = stack.pop()
                numOfDays[prevI] = i - prevI

            stack.append(i)

        return numOfDays