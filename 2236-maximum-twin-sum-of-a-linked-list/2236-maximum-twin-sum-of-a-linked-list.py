class Solution(object):
    def pairSum(self, head):

        fast = slow = head
        result = 0
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
            if result < (rev.val + head.val):
                result = rev.val + head.val
            # result = max(rev.val + head.val, result)
            rev = rev.next
            head = head.next
        
        return result

