#Q: https://leetcode.com/problems/linked-list-cycle/
class Solution:
    #Pattern: Fast slow two pointer - O(N)/O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow,fast = head,head

        while fast!=None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False