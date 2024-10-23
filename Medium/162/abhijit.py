class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def check(low,high):
            if low > high:
                # invalid search 
                return -1
            mid = (low + high ) // 2 # find the mid value
            print(nums[low:high+1],mid)
            #checking the corner cases
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    return -1
            if mid == len(nums) -1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    return -1
            
            # check if the current spot is a mid
            if nums[mid -1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
                
            left = check(low,mid - 1)
            right = check(mid + 1,high)
            if left != -1 and right == -1:
                return left
            elif right != -1 and left == -1:
                return right
            elif left == -1 and right == -1:
                return -1
            else:
                return left
                
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        return check(0,len(nums)-1)

            