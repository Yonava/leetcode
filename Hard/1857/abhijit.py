import string
from collections import defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree_count = [0] * len(colors)
        seen_nodes = {}

        def aggregateColours(parent, child):
            for colour in child:
                parent[colour] = max(parent[colour], child[colour])

        def dfs(node, seen_set):
            if node in seen_set:
                return -1  # cycle detected

            if node in seen_nodes:
                return seen_nodes[node].copy()

            seen_set.add(node)

            curr_counts = {char: 0 for char in string.ascii_lowercase}
            curr_counts[colors[node]] = 1

            for neighbor in graph[node]:
                result = dfs(neighbor, seen_set)
                if result == -1:
                    return -1
                temp = {char: 0 for char in string.ascii_lowercase}
                aggregateColours(temp, result)
                for c in temp:
                    if c == colors[node]:
                        curr_counts[c] = max(curr_counts[c], temp[c] + 1)
                    else:
                        curr_counts[c] = max(curr_counts[c], temp[c])

            seen_set.remove(node)
            seen_nodes[node] = curr_counts.copy()
            return curr_counts

        for u, v in edges:
            graph[u].append(v)
            in_degree_count[v] += 1

        max_val = 0
        for i in range(len(colors)):
            result = dfs(i, set())
            if result == -1:
                return -1
            max_val = max(max_val, max(result.values()))

        return max_val
