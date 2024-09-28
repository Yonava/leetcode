# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recurHelper(self,parent,l,r,nums):
        if l > r:  
            return
        
        mid = (l + r) // 2 
        print(f"currently L: {l} R: {r} mid:", nums[mid])  # Debug print
        
        node = TreeNode(val=nums[mid])  
        
    
        if node.val < parent.val:
            parent.left = node
        else:
            parent.right = node
        

        self.recurHelper(node, l, mid - 1, nums) 
        self.recurHelper(node, mid + 1, r, nums) 

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l,r = 0 , len(nums) - 1
        mid = (l+r) //2
        root = TreeNode(nums[mid])
        self.recurHelper(root,mid + 1,r,nums)
        self.recurHelper(root,l,mid -1,nums)

        return root