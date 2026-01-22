class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        tracker = nums.copy()

        max_val = float("-inf")

        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] + 1 != nums[j] and nums[i] - 1 != nums[j]:
                    tracker[i] = max(tracker[i], nums[i] + tracker[j]) 
            max_val = max(max_val, tracker[i])
    
        return max_val
            
        
# reduction to house robber
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ## APPROACH : DP ##
        """
        1. [2,2,3,3,3,4], one observation is assume array is sorted, if you choose 2, we cannot choose 3. or If choose 3, cannot chose 4. or If choose 4 cannot chose 3.
        2. Another observation is (ONLY WHEN PLACED IN SORTED ORDER) replacing multiple copies of same number with its sum doesnt matter.
        3. Now the prob is reduced to House robber problem, where you can only rob houses if they are one distance apart. What is the max money he can get by robbing such.
        4. We consider money is 0 for missing houses. [2,2,3,3,3,4] indicates house 1 with 0, house 2 with money 4, house 3 with money 9, house 4 with money 4. Total number of houses is max of the nums list.
        """
        if not nums : return 0
        house = [0] * (max(nums)+1)
        for num in nums:
            house[num] += num
        
        print(house)

        dp = [0]*(len(house)+1)
        for i in range(1,len(house)):
            dp[i] = max(house[i]+dp[i-2], dp[i-1])
        return max(dp[-1],dp[-2])
        