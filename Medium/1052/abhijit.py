class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        if he is not grumpy we can just add it to the sum.
        find window of size minutes where # of customers dissatisfied is the largest

        we use a window of size minutes to find max customers converted


        """

        if len(customers) <= minutes:
            # all customers satisfied
            return sum(customers)
        
        max_conversions = 0
        curr_conversions = 0
        l = 0
        for r in range(len(customers)):
            if r - l >= minutes:
                max_conversions = max(max_conversions, curr_conversions)
                if grumpy[l] == 1:
                    curr_conversions -= customers[l]
                if grumpy[r] == 1:
                    curr_conversions += customers[r]
                
                max_conversions = max(max_conversions, curr_conversions)
                r += 1
                l += 1
            else:
                if grumpy[r] == 1:
                    curr_conversions += customers[r]
                r += 1
        
        sat_customers = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                sat_customers += customers[i]
        print(sat_customers, max_conversions)
        return sat_customers + max_conversions

                
