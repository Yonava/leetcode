class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start: int) -> List[int]:
            dist = [-1] * len(edges)
            q = deque()
            q.append((start, 0))
            visited = set()

            while q:
                curr, d = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                dist[curr] = d
                neighbor = edges[curr]
                if neighbor != -1 and neighbor not in visited:
                    q.append((neighbor, d + 1))
            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        min_dist = float('inf')
        result = -1
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i
        return result
