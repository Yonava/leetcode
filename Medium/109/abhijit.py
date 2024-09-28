# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(arr: List[int], s: int, e: int) -> Optional[TreeNode]:
            if s > e:
                return None
            mid = s + (e - s) // 2
            root = TreeNode(arr[mid])
            root.left = helper(arr, s, mid - 1)
            root.right = helper(arr, mid + 1, e)
            return root

        ar = []
        while head:
            ar.append(head.val)
            head = head.next

        n = len(ar)
        root = helper(ar, 0, n - 1)
        return root