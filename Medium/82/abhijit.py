class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currPointer = ListNode(-1, head)  # Just as a helper for linking; not used for return
        currPointer.next = head
        currentNode = head

        if head is None:
            return head

        while currentNode and currentNode.next:
            if currentNode.val != currentNode.next.val:
                if currPointer.next == currentNode:
                    currPointer = currentNode
                else:
                    if currPointer.next == head:
                        head = currentNode.next
                    currPointer.next = currentNode.next
            currentNode = currentNode.next

        # Handle the last group
        if currPointer.next != currentNode:
            if currPointer.next == head:
                head = currentNode.next
            currPointer.next = currentNode.next

        return head