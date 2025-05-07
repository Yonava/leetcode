class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                dist = manhattan(points[i], points[j])
                edges.append((dist, i, j)) 

        # sort to ensure that we are picking the shortest edge first
        edges.sort()

        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return False
            parent[yr] = xr
            return True

        cost = 0
        edges_used = 0
        for weight, u, v in edges:
            if union(u, v):
                cost += weight
                edges_used += 1
                if edges_used == n - 1:
                    break
        
        return cost
