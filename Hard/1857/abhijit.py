from typing import List
import string

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        from collections import defaultdict

        # Build graph and in-degree count
        graph = defaultdict(list)
        in_degree_count = {i: 0 for i in range(len(colors))}

        for src, dst in edges:
            graph[src].append(dst)
            in_degree_count[dst] += 1

        seen_nodes = {}  # memoization
        visiting = set()  # for cycle detection

        # Helper: aggregate max color counts
        def aggregate_max(parent, child):
            for c in string.ascii_lowercase:
                parent[c] = max(parent[c], child[c])

        # DFS with cycle detection and memoization
        def dfs(node: int) -> dict or int:
            if node in visiting:
                return -1  # cycle found
            if node in seen_nodes:
                return seen_nodes[node]

            visiting.add(node)
            current_color_count = {c: 0 for c in string.ascii_lowercase}

            for neighbor in graph[node]:
                result = dfs(neighbor)
                if result == -1:
                    return -1  # propagate cycle
                aggregate_max(current_color_count, result)

            visiting.remove(node)

            # Increment this node's color
            current_color_count[colors[node]] += 1
            seen_nodes[node] = current_color_count
            return current_color_count

        # Try DFS from all nodes
        final_result = 0
        for node in range(len(colors)):
            if node not in seen_nodes:
                result = dfs(node)
                if result == -1:
                    return -1
                final_result = max(final_result, max(result.values()))

        return final_result
