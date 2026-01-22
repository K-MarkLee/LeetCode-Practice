# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        prev = None
        ahead = head.next

        while ahead:
            head.next = prev
            prev = head
            head = ahead
            ahead = ahead.next
        head.next = prev

        return head