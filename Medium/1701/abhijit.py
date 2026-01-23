class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish_time = float('-inf')
        total_wait = 0
        for arrival, wait in customers:
            if finish_time < arrival:
                finish_time = arrival
            finish_time = finish_time + wait
            total_wait += finish_time - arrival


        return total_wait/ len(customers)

