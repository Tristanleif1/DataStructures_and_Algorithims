class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Oklog(N) time using a heap/heapify
        #Quick select algorithim O(N)



        #N(LogN) solution
        # nums.sort()
        # return nums[len(nums) - k]

        #Quick select algorithim does not run well on some of the test cases
        #On the average case, it beats the sorting apporach algorithim
        #Quickselect is a good algorithim to know

       k = len(nums) - k
       def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:   return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else:       return nums[p]

       return quickSelect(0, len(nums) - 1)