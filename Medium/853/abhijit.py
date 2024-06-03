class Solution:
    # I learnt that we can sort the data to make it easier. I figured sorting would be better. However, I didn't apply the sorting
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_right_to_left = sorted(zip(position, speed), reverse=True)

        bottleneck = float('-inf')
        fleets = 0

        for d, s in cars_right_to_left:
            remaining_dist = target - d
            time_to_reach_target = (remaining_dist / s)

            if time_to_reach_target > bottleneck:
                bottleneck = time_to_reach_target
                fleets += 1

        return fleets
        
'''

'''