# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Part 1 - Find the middle and split
        fast = head
        slow = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        # Part 2 - Reverse the second half
        prev=None
        curr=head2
        next=None
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next

        # Part 3 - Merge Alternatively
        l1 = head
        l2 = prev

        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2
