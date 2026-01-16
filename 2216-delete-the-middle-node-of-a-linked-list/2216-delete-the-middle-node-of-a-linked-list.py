class Solution(object):
    def deleteMiddle(self, head) :
        slow = head
        fast = head
        prev = None
        if head is None or head.next is None :
            return None
        while fast and fast.next :
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        slow.next = None
        return  head