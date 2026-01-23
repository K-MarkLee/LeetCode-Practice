class Solution(object):
    def pairSum(self, head):

        fast = slow = head
        result = 0
        while fast:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        rev = slow
        
        while rev.next:
            ahead = rev.next
            rev.next = prev
            prev = rev
            rev = ahead
        rev.next = prev

        while rev:
            temp = rev.val + head.val
            if result < temp:
                result = temp
            rev = rev.next
            head = head.next
        
        return result

