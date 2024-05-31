class Solution:
    def trap(self, height: List[int]) -> int:
        water_collected = 0
        l,r = 0,0
        sumSoFar = 0
        while r < len(height) -1:
            r += 1
            if height[l] > height[r]:
                sumSoFar += height[l] - height[r]
            else:
                l = r
                water_collected += sumSoFar
                sumSoFar = 0

        if l != r:
            left_place = l
            sumSoFar = 0
            l = r
            while r >= left_place:
                r -= 1
                if height[l] > height[r]:
                    sumSoFar += height[l] - height[r]
                else:
                    l = r
                    water_collected += sumSoFar
                    sumSoFar = 0
                
        return water_collected
        