class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # make a graph from the edges
        adjacency_list = {}

        if not edges:
            return n


        for edge in edges:
            to, end = edge[0], edge[1]

            # Add 'end' to the neighbors of 'to'
            if to not in adjacency_list:
                adjacency_list[to] = set()
            adjacency_list[to].add(end)

            # Add 'to' to the neighbors of 'end'
            if end not in adjacency_list:
                adjacency_list[end] = set()
            adjacency_list[end].add(to)

        
        # start a bfs from each node
        seen = set()
        component_count = 0

        def bfs(start):
            q = deque()
            q.append(start)

            while q:
                curr = q.popleft()
                for neighbour in adjacency_list[curr]:
                    if neighbour not in seen:
                        q.append(neighbour)
                        seen.add(neighbour)
    


        for node in adjacency_list.keys():
            if node not in seen:
                bfs(node)
                component_count += 1

        return component_count

        