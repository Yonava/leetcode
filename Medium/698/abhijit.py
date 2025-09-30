class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        prune_val = total // k
        
        nums.sort(reverse=True)
        tracker = [0] * k
        
        def dfs(i):
            if i == len(nums):  # all numbers placed
                for i in range(k):
                    if tracker[i] != prune_val:
                        return False
                return True
            for subset in range(k):
                if tracker[subset] + nums[i] <= prune_val:
                    tracker[subset] += nums[i]
                    if dfs(i + 1):
                        return True
                    tracker[subset] -= nums[i]
                # symmetry pruning: if this subset is still empty after backtracking,
                # no point in trying the same number in other empty subsets
                if tracker[subset] == 0:
                    break
            return False
    
        return dfs(0)



        