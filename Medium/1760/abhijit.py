class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        total_bags = len(nums) + maxOperations
        total_balls = sum(nums)
        l, r = 1, max(nums)

        def canAchieve(penalty):
            ops_needed = 0
            for n in nums:
                # How many bags do we need to split n into?
                # ceil(n / penalty) bags, which requires ceil(n/penalty) - 1 splits
                ops_needed += (n - 1) // penalty
            return ops_needed <= maxOperations

        while r > l:
            mid = (l + r) // 2
            if canAchieve(mid):
                r = mid
            else:
                l = mid + 1
        return r