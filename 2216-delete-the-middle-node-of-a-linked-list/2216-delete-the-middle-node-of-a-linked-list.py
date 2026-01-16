class Solution(object):
    def deleteMiddle(self, head):
        left = head
        right = head
        prev = head

        if head is None or head.next is None:
            return None
        
        while right and right.next:
            prev = left
            left = left.next
            right = right.next.next
        
        prev.next = left.next
        left.next = None
        return head
