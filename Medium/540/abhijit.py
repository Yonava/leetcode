class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # Ensure mid is even so we always compare pairs safely
            if mid % 2 == 1:
                mid -= 1

            print(l,r, mid)

            # Valid pair → single is to the right
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                # Broken pair → single is here or to the left
                r = mid

        return nums[l]

# my solution had the right idea. however, i could have spent a minute
# understanding how the indexes can give us more information

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        single non duplicate
        tracker -> set
        o(n) -> if already in set remove. else add


        array is odd length. 
        we find middle. 
        l, m-1, m, m + 1, r
    
        if m -1 == m and r - m + 1 is even then it does not exist in m + 1 to r
        if m + 1 == m and l - m - 1 is even then it does not exist in l to m -1
        if m - 1 != m and m + 1 != m:
            return m
        """

        l, r = 0, len(nums) - 1
        
        while r >= l:
            mid = (l + r) // 2
            print(l,r)

            if nums[mid -1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if nums[mid - 1] == nums[mid]:
                if mid % 2 == 0:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid + 1] == nums[mid]:
                if mid % 2 == 0:
                    # mid is even
                    l = mid + 1
                else:
                    r = mid - 1
                
        print("final",l,r)
            
        return nums[l]
            