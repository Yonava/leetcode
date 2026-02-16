class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        this is an o(n) solution.
        we start from r = len(heights) - 1
        max_height = f

        """
        tallest = float("-inf")
        r = len(heights) - 1
        can_see = []
        while r >= 0:
            if heights[r] > tallest:
                can_see.append(r)
                tallest = heights[r]
            r -= 1

        can_see.reverse()
        
        return can_see
            