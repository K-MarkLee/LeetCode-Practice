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
        slow = fast = head
        result = 0

        while fast:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        rev = slow

        while rev:
            ahead = rev.next
            rev.next = prev
            prev = rev
            rev = ahead

        while prev:
            temp = prev.val+head.val
            if temp > result:
                result = temp
            prev = prev.next
            head = head.next

        return result 
        