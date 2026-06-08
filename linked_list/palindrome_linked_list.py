#Q: https://leetcode.com/problems/palindrome-linked-list/
class Solution:
    #Pattern: Two pointer fast slow - O(N)/O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # find the middle indicated by the slow pointer
        slow, fast = head, head
        left_pointer = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.nex
        # reverse the second half of the list
        prev = None
        curr = slow

        while curr != None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        # Compare from both sides of the list as second half is reversed
        right_pointer = prev
        while right_pointer != None:
            if left_pointer.val != right_pointer.val:
                return False
            else:
                left_pointer = left_pointer.next
                right_pointer = right_pointer.next
        return True


