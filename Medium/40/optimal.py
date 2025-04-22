from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                results.append(path.copy())
                return
            if remaining < 0:
                return

            prev = -1  # Track previous value to skip duplicates
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return results