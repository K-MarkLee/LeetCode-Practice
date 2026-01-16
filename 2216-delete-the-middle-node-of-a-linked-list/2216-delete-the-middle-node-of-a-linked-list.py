# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while right and right.next:
            left = left.next
            right = right.next.next
        else:
            left.next = left.next.next
        
        return dummy.next