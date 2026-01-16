class Solution(object):
    def deleteMiddle(self, head):
        left = head
        right = head
        prev = head

        if not head or not head.next:
            return None
        
        while right and right.next:
            prev = left
            left = left.next
            right = right.next.next
        
        prev.next = left.next

        return head
