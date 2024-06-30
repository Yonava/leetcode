class Solution:
    def findMaxWidth(self, arr, curr_index):
        min = arr[curr_index]
        l = curr_index
        r = curr_index
        while l >= 1:
            if arr[l-1] >= min:
                l -= 1
            else:
                break
        while r <= len(arr) - 2:
            if arr[r + 1] >= min:
                r += 1
            else:
                break
        return [l,r]

    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            if i > 0 and heights[i - 1] == heights[i]:
                continue
            l, r = self.findMaxWidth(heights,i)
            area = heights[i] * ( r - l + 1)
            res = max(area,res)

        return res
        