class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # values.sort() # we can sort this out so we can make the greedy choice
        # h = [(values[0], 1), (values[1], 1), (values[2], 1)]
        # heapq.heapify(h)
        # # keep track of the total score
        # areaSum = values[0] * values[1] * values[2] 
        
        # N = len(values)
        
        # # each vertex can be part of max triangles
        # max_triangles = N - 2

        # for i in range(3,N):
        #     print(h)
        #     while h[0][1] >= max_triangles:
        #         heapq.heappop(h)    

        #     v1, v1_triangle = heapq.heappop(h)
        #     v2, v2_triangle = heapq.heappop(h)
        #     curr_v = values[i]

        #     areaSum += curr_v * v1 * v2 
            
        #     if v1_triangle + 1 < max_triangles:
        #         heapq.heappush(h,(v1,v1_triangle + 1))
            
        #     if v2_triangle + 1 < max_triangles:
        #         heapq.heappush(h,(v2, v2_triangle + 1))
            
        #     heapq.heappush(h,(curr_v, 1))

        # return areaSum

        @cache
        def dp(i,j):
            if j - i < 2:
                return 0
            
            res = float("inf")
            for k in range(i + 1, j):
                curr = values[i] * values[j] * values[k]
                res = min(res, curr + dp(i,k) + dp(k,j))
            
            return res
        
        return dp(0, len(values) - 1)