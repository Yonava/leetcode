class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftmost(nums, target):
            l, r = 0, len(nums) - 1
            leftmost = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    leftmost = mid
                    r = mid - 1  # Continue searching to the left for the leftmost occurrence
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return leftmost

        def findRightmost(nums, target):
            l, r = 0, len(nums) - 1
            rightmost = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    rightmost = mid
                    l = mid + 1  # Continue searching to the right for the rightmost occurrence
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return rightmost

        leftmost = findLeftmost(nums, target)
        rightmost = findRightmost(nums, target)
        return [leftmost, rightmost] if leftmost != -1 else [-1, -1]
