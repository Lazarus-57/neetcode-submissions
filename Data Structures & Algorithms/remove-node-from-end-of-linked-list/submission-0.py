# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #use Lloyd's slow and fast pointers in a smart way
        dummy=ListNode(0)
        dummy.next=head
        
        slow = dummy
        fast = dummy

        for i in range (1,n+1):
            fast=fast.next

        while fast.next is not None:
            slow=slow.next
            fast=fast.next

        #remove node by removing pointer to node
        slow.next=slow.next.next

        return dummy.next