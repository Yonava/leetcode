"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def findIndex(self,head, node):
        index = 0
        if node == None:
            return -1
        while head != None:
            
            if head == node:
                print("returning index", index)
                return index 
            else:
                index +=1
                head = head.next
        return -1
        
        
    def recursivelyBuild(self,originalHead,head,index,tracker):
        if head == None:
            return None
        p1 = originalHead
        i = self.findIndex(p1,head.random)
        print(i)
        new_node = Node(head.val,self.recursivelyBuild(originalHead,head.next,index + 1, tracker), i)
        tracker[index] = new_node
        return new_node


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        go through each each node and create the current node (deep copy of current node)
        '''
        nodes_created = {}
        created_index = 0
        p1 = head
        rtn_list = self.recursivelyBuild(head,p1,0,nodes_created)
        p2 = rtn_list
        while p2 != None:
            if p2.random == -1:
                p2.random = None
            else:
                p2.random = nodes_created[p2.random]
            p2 = p2.next
        
        return rtn_list