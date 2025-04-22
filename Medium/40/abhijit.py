class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        possible_picks = []
        def recurSearch(val, past_picks, options):
            nonlocal possible_picks

            if val < 0:
                return
            if len(options) == 0 and val != 0:
                return 
            if val == 0:
                possible_picks.append(past_picks.copy())
                return
            current_picks = past_picks.copy()
            seen = set()
            while options:
                pick = options.pop()
                if pick in seen:
                    continue
                current_picks.append(pick)
                recurSearch(val - pick,current_picks,options.copy())
                seen.add(pick)
                current_picks.pop()
        
        recurSearch(target,[],candidates)
        return possible_picks