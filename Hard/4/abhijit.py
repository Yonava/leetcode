"""
    we could potentially append the arrays based on what the 0th index looks like.
    if nums1[0] > nums2[0], nums2 + nums1 else: nums1 + nums2
    now we have 2 pointers, 
    p1: at the start of the array
    p2: at the at start of the second array once its merged, m or n (Depending on which array is placed)

    we know that the first 2 numbers are nums1[0] and nums2[0]
    now we can keep moving these pointers until we are at a n + m /2 and n+m/2 + 1
    -> if the sum is odd, then we can just return the pointer at n + m/2
    -> if the sum is even, then we have to calculate the median. 

    """

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Handle cases where one of the arrays is empty
        if not nums1:
            n = len(nums2)
            return nums2[n//2] if n % 2 == 1 else (nums2[n//2 - 1] + nums2[n//2]) / 2
        if not nums2:
            n = len(nums1)
            return nums1[n//2] if n % 2 == 1 else (nums1[n//2 - 1] + nums1[n//2]) / 2

        # Total length of the combined arrays
        total_length = len(nums1) + len(nums2)
        half_len = total_length // 2

        # Two pointers
        p1, p2 = 0, 0

        # To store the last two numbers we encounter while traversing
        current, previous = 0, 0

        # Move pointers until we reach the middle point
        for i in range(half_len + 1):
            previous = current  # Store the last number in case we need it for the even case
            if p1 < len(nums1) and (p2 >= len(nums2) or nums1[p1] <= nums2[p2]):
                current = nums1[p1]
                p1 += 1
            else:
                current = nums2[p2]
                p2 += 1

        # If total length is odd, return the middle element
        if total_length % 2 == 1:
            return current
        # If total length is even, return the average of the last two elements
        else:
            return (current + previous) / 2
