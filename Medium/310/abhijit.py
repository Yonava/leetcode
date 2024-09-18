class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # create one tree and then calculate height of tree from each possible node
        
        adjacency_list = {}

        if not edges:
            return [0]

        for node_one, node_two in edges:
            # create tree
            if node_one not in adjacency_list:
                adjacency_list[node_one] = set()
            adjacency_list[node_one].add(node_two)

            if node_two not in adjacency_list:
                adjacency_list[node_two] = set()
            adjacency_list[node_two].add(node_one)
        
        seen = set()  
        def calc_height(curr,parent):
            if curr in seen:
                return 0

            max_height = float("-inf")

            # add self to seen, before exploring
            seen.add(curr)

            for child in adjacency_list[curr]:
                if child == parent:
                    continue
                height = 1 + calc_height(child,curr)
                max_height = max(height,max_height)

            return 0 if max_height == float("-inf") else max_height
        
        heights = []
        min_height = float("inf")
        for root in adjacency_list:
            seen = set()
            height = calc_height(root,None)
            min_height = min(height,min_height)
            heights.append((height,root))
            
        return [node for height, node in heights if height == min_height]
