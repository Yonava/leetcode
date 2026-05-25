class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            # if mid is target
            if nums[mid] == target:
                return True
            # if right is sorted
            if nums[mid] < nums[r]:
                # if target is in right
                if nums[mid] <= target <= nums[r]:
                    l=mid+1
                # if target is in left
                else:
                    r=mid-1
            # if right is not sorted (meaning left has to be sorted)
            elif nums[mid] > nums[r]:
                # if target is in left
                if nums[l] <= target <= nums[mid]:
                    r=mid-1
                # if target is in right
                else:
                    l=mid+1
            # if right is same as mid
            else:
                r -= 1

        return False

"""
since we are using the right most position to determine which half is sorted,
we can encounter a situation where the right most position is the same as mid, which means we cannot determine which half is sorted. In this case, 
we can just decrement the right pointer by 1 and continue the search
"""