class Solution:
    def numGreaterThan(self,n, nums):
        counter = 0
        for num in nums:
            if num >= n:
                counter +=1
        
        return counter


    def specialArray(self, nums: List[int]) -> int:
        l,h = 0 , max(nums)
        while h >= l:
            mid = (h + l) // 2
            print(mid)
            val = self.numGreaterThan(mid,nums)
            if val == mid:
                return val
            if val < mid:
                h = mid - 1
            else:
                l = mid + 1
        
        print("l",l)
        print('h',h)
        return -1