def solution(n, edges):
    if len(edges) != n - 1:
        return False
        
    # Build adjacency list
    nodes = {i: [] for i in range(n)}
    for start, end in edges:
        nodes[start].append(end)
        nodes[end].append(start)
    
    # 0 = Unvisited, 1 = Exploring, 2 = Explored
    state_array = [0] * n 
    
    # Stack stores: (current_node, parent_node)
    stack = [(0, -1)]
    state_array[0] = 1 # Mark start node as Exploring
    
    while stack:
        current_node, parent = stack.pop()
        
        for neighbor in nodes[current_node]:
            if neighbor == parent:
                continue # Skip the edge we just came from
                
            if state_array[neighbor] == 1:
                # We found a node currently being explored -> TRUE CYCLE
                return False
                
            if state_array[neighbor] == 0:
                # Found an unvisited node -> Mark as Exploring and push to stack
                state_array[neighbor] = 1
                stack.append((neighbor, current_node))
                
        # Once we've checked all neighbors, this node is officially fully explored
        state_array[current_node] = 2
        
    # If any node remains 0, the graph is disconnected
    return all(state == 2 for state in state_array)