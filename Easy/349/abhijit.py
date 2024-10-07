# my solution
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_a = set(nums1)
        set_b = set(nums2)
    
        if len(set_a) > len(set_b):
            diff_one = set_a - set_b
            return set_a - diff_one
        else:
            diff_one = set_a - set_b
            return set_a - diff_one
        
    