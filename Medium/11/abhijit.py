class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max area. Height by the values of the numbers in the array. 
        # and the width is the distance between the numbers in the array
        # we need to find pars of acceptable heights.
        # we need to sort or like order the pairs such that we have the pairs with the greatest heights.
        # We need to find the area by comparing the index values and finding the height x (greater index - lower index)

        # O(n^2) method:
        # area = []
        # for i in range(len(height)):
        #     for j in range (len(height)):
        #         width = abs(i-j)
        #         if(height[j] <= height[i]):
        #             area.append(width * height[j])
        #         else:
        #             area.append(width * height[i])
        # return max(area)
        
        low, high = 0, len(height) - 1
        area = []
        while high > low:
            if(height[low] <= height[high]):
                area.append((high - low) * height[low])
                low += 1
            else:
                area.append((high - low) * height[high])
                high -= 1
        
        return max(area)