#Q: https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    #Pattern: Slow Fast two pointers - O(N)/O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow