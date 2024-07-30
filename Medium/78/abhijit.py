class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(length, curr_arr, choices):
            if length == len(nums):
                res.append(curr_arr.copy())
                return
            res.append(curr_arr.copy())
            for choice in choices:
                curr_arr.append(choice)
                filtered_choice = [x for x in choices if x != choice]
                backTrack(length + 1,curr_arr,filtered_choice)
                curr_arr.pop()

        backTrack(0,[],nums)
        tracker = {}
        final = []
        for subset in res:
            subset.sort()
            str_id = "".join([str(x) for x in subset])
            print(str_id)
            if tracker.get(str_id,0) > 0:
                continue
            else:
                tracker[str_id] = 1
                final.append(subset)
        return final