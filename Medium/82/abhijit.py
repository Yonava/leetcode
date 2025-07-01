class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        current = head

        while current:
            # Check if current is start of a duplicate sequence
            has_duplicate = False
            while current.next and current.val == current.next.val:
                current = current.next
                has_duplicate = True
            
            if has_duplicate:
                # Skip all duplicates
                prev.next = current.next
            else:
                # No duplicate, move prev
                prev = prev.next
            
            current = current.next
        
        return dummy.next
