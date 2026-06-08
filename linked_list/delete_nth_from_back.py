#Q: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#Pattern: Slow Fast two pointers - O(N)/O(1)
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow,fast = head,head


    #remove the node slow is pointed to.
    while fast !=None and n!=0:
      fast = fast.next
      n -=1


    if(fast == None): return slow.next

    while fast != None:
      tail = slow
      slow = slow.next
      fast = fast.next

    tail.next = slow.next

    return head