# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialised_string = ""
        def preOrderTrav(node):
            nonlocal serialised_string
            if node == None:
                return
            elif node.left == None and node.right == None:
                serialised_string += "#%,%"
                return
            my_vals = []
            my_vals.append(str(node.left.val) if node.left is not None else "%")
            my_vals.append(str(node.right.val) if node.right is not None else "%")
            serialised_string += f"#{my_vals[0]},{my_vals[1]}"
            preOrderTrav(node.left)
            preOrderTrav(node.right)
        preOrderTrav(root)
        return f"#{root.val if root else '%'}" + serialised_string        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_pairs = data.split("#")
        current_pos = 2
        def recurCreate(parentNode):
            nonlocal current_pos
            l,r = node_pairs[current_pos].split(",")
            if l == '%' and r == '%':
                parentNode.left == None
                parentNode.right == None
                return
            elif l == "%":
                parentNode.left == None
                parentNode.right = TreeNode(int(r))
                current_pos += 1
                recurCreate(parentNode.right)
            elif r == "%":
                parentNode.right == None
                parentNode.left = TreeNode(int(l))
                current_pos += 1
                recurCreate(parentNode.left)
            else:
                parentNode.left = TreeNode(int(l))
                parentNode.right = TreeNode(int(r))
                current_pos +=1
                recurCreate(parentNode.left)
                current_pos +=1
                recurCreate(parentNode.right)
        

        root = node_pairs[1]
        if root == "%":
            return None
        root = TreeNode(int(root))
        recurCreate(root)   
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))