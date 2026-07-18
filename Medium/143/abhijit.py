# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def display(h):
            arr = []
            while h is not None:
                arr.append(h.val)
                h = h.next
            print(arr)


        if head is None or head.next is None:
            return head
        start = head
        curr = head
        head.prev = None

        
        # print("here 0")
        while curr.next is not None:
            curr.next.prev = curr
            curr = curr.next

        last = curr
        first = head
        # print("here 1")
        while first.next != last and first != last:
            first_n = first.next
            first.next = last
            last.next = first_n
            last = last.prev
            last.next = None
            first = first.next.next
            # display(head)
            # print(first.val, last.val)
        
        # print("here 2")
        # while start.next is not None:
        #     start.prev = None
        
        return start

