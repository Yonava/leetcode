class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # If the target is found at mid, return the index
            if nums[mid] == target:
                return mid
            
            # Determine which part is sorted
            if nums[l] <= nums[mid]:
                # Left part is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Search the left side
                else:
                    l = mid + 1  # Search the right side
            else:
                # Right part is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Search the right side
                else:
                    r = mid - 1  # Search the left side
        
        return -1  # Target not found
