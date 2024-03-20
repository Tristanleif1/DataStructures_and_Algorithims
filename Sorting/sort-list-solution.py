class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Merge Sort (nLogN) time complexity
        #Recursive approach --> logN space complexity

        if not head or not head.next:
            return head

        #split the list into two halfs
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        tail = dummy = ListNode()
        #tail variable is the position where we insert a merged node at
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        #We return dummy.next b/c if we return dummy we are returning an unnecessary node we created
        return dummy.next