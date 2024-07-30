class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        MaxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                MaxArea = max(MaxArea, height * (i - index))
                start = index
            stack.append((start,h))

        for i,h  in stack:
            MaxArea = max(MaxArea, h * (len(heights) - i))
        
        return MaxArea
        