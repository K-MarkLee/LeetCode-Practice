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
        if not head or not head.next:
            return head

        if not head.next.next:
            return head.val + head.next.val

        slow = head
        fast = head.next
        while fast.next:
            fast = fast.next.next
            slow = slow.next
        

        prev = slow
        rev = slow.next
        ahead = rev.next

        while ahead:
            rev.next = prev
            prev = rev
            rev = ahead
            ahead = ahead.next
        rev.next = prev

        result = float('-inf')
        while head != slow.next and rev:
            result = max(result, (head.val + rev.val))
            head = head.next
            rev = rev.next

        return result
        