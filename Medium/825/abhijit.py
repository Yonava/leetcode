class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        """
        Lower Bound: The first index where ages[mid] > 0.5 * age + 7.

        Upper Bound: The last index where ages[mid] <= age.

        """
        ages.sort()
        count = 0

        def find_first_valid(target_val):
            l, r = 0, len(ages) - 1
            first_idx = len(ages)
            while l <= r:
                mid = (l + r) // 2
                if ages[mid] > target_val:
                    first_idx = mid
                    r = mid - 1  
                else:
                    l = mid + 1
            return first_idx

        def find_last_valid(target_val):
            l, r = 0, len(ages) - 1
            last_idx = -1
            while l <= r:
                mid = (l + r) // 2
                if ages[mid] <= target_val:
                    last_idx = mid
                    l = mid + 1  
                else:
                    r = mid - 1
            return last_idx

        for i, age in enumerate(ages):
            # Rule: age[B] > 0.5 * age[A] + 7
            # If age is 14 or less, 0.5 * 14 + 7 = 14. 
            # No one can be > 14 AND <= 14.
            if age <= 14:
                continue
            
            lower_bound = find_first_valid(0.5 * age + 7)
            upper_bound = find_last_valid(age)
            
            if upper_bound >= lower_bound:
                count += upper_bound - lower_bound

        return count