# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast = slow = head
        result = float('-inf')
        while fast:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        rev = slow
        ahead = slow.next

        while ahead:
            rev.next = prev
            prev = rev
            rev = ahead
            ahead = ahead.next
        rev.next = prev

        while rev:
            result = max(rev.val + head.val, result)
            rev = rev.next
            head = head.next
        
        return result

