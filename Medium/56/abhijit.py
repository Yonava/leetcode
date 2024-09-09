# sorting helps with merging

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        current_interval = intervals[0]

        for i in range(1,len(intervals)):
            if current_interval[1] >= intervals[i][0]:
                if current_interval[0] > intervals[i][1]:
                    # we are overshooting
                    result.append(current_interval)
                    current_interval = intervals[i]

                if current_interval[0] >= intervals[i][0]:
                    current_interval[0] = intervals[i][0]
                
                if current_interval[1] < intervals[i][1]:
                    current_interval[1] = intervals[i][1]
        
            else:
                result.append(current_interval)
                current_interval = intervals[i]

        result.append(current_interval)

        
        return result
