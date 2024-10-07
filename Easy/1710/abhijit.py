class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x: x[1], reverse=True) # sort in decreasing size of boxes. 
        curr_size = truckSize
        total_box = 0
        for box_type, box_amt in boxTypes:
            curr_amt_of_boxes = box_type
           
            while curr_size and curr_amt_of_boxes:
                total_box += box_amt
                curr_amt_of_boxes -= 1
                curr_size -= 1
        
        return total_box
