# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative O(n) Solution where you iterate through linked list and swap the next to the previous node
        
        prevHead = None
        currHead = head
        
        while currHead != None:
            nextHead = currHead.next
            currHead.next = prevHead
            prevHead = currHead
            currHead = nextHead
        return prevHead
            