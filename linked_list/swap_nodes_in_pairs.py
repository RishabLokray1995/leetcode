# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Q: https://leetcode.com/problems/swap-nodes-in-pairs/

#Pattern: Slow Fast two pointers - O(N)/O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None: return head
        tail = ListNode()

        result = tail

        slow = head

        while slow != None and slow.next != None:
            fast = slow.next

            #set the next invariant
            next_s = fast.next
            tail.next = fast

            #nodes to swap
            # slow and fast


            #swap
            fast.next = slow
            slow.next = next_s

            #move tail ahead
            tail = slow
            slow = next_s
        return result.next




