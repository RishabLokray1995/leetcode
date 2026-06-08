# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Q: https://leetcode.com/problems/merge-k-sorted-lists/
class PqNode():
  def __init__(self,node):
    self.node = node

  #if the comaprison gets to this node then just return the first one
  def __lt__(self,other):
    return self


from heapq import heapify,heappush,heappop

class Solution:
  #runs out of memory because you are pushing all nodes into the heap at once, and if there are k lists with N nodes each then you are pushing kN nodes into the heap which is too much for memory. You only need to push k nodes at a time which is the head of each list, and then when you pop one out you push the next one from that list.

  # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  #     minheap = []
  #     heapify(minheap)

  #     for l in lists: #k times
  #         head = l
  #         while head!=None: #max list is N = kNlogN
  #             heappush(minheap,(head.val, PqNode(head)))
  #             head = head.next

  #     dummy = ListNode()
  #     head = dummy

  #     while len(minheap)!=0:
  #         smallest_node_val,pqNode = heappop(minheap)
  #         dummy.next = pqNode.node
  #         dummy = dummy.next

  #     return head.next

  #Pattern: Linked list + heapq, O(NLogK) = max height of heap is k so logK, you loop this max N times which is the size of largest list.
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    minheap = []
    heapify(minheap)
    for l in lists: # add all heads for starting point.
      if(l!=None): heappush(minheap,(l.val, PqNode(l)))

    dummy = ListNode()
    head = dummy

    #take smallest out, and push next one immediately
    while len(minheap)!=0:
      smallest_node_val,pqNode = heappop(minheap)
      dummy.next = pqNode.node
      dummy = dummy.next

      next_node = pqNode.node.next
      if(next_node != None):
        heappush(minheap, (next_node.val,PqNode(next_node)))

    return head.next





