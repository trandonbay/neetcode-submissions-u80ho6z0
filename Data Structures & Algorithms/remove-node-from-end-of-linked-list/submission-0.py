# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = cur = delay = ListNode(0, head)

        while cur.next:
            cur = cur.next

            if n > 0:
                n -= 1
            else:
                delay = delay.next

        delay.next = delay.next.next

        return dummy.next