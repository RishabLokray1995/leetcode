#Q: https://leetcode.com/problems/reverse-linked-list/
class Solution:
    # Pattern: 2 pointer techinique - always start next,curr = head : O(N)/O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while (curr != None):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev
