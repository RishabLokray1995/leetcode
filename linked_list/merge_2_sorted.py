#Q: https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    # Pattern: Two pointer - O(N+M)/O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = list1
        l2_head = list2
        tail = ListNode()
        answer = tail

        while l1_head != None and l2_head != None:
            if l1_head.val <= l2_head.val:
                tail.next = l1_head
                tail = tail.next
                l1_head = l1_head.next
            else:
                tail.next = l2_head
                tail = tail.next
                l2_head = l2_head.next

        if (l2_head):
            tail.next = l2_head
        else:
            tail.next = l1_head

        return answer.next
