class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()
        def bfs(sum, arr):
            if sum == target:
                # accept
                res.append(arr.copy())
                return 0
            if sum > target:
                print("terminating", sum, arr)
                # terminate
                return -1

            # propogate
            for candidate in candidates:
                arr.append(candidate)
                val = bfs(sum + candidate,arr)
                if val == -1:
                    arr.pop()
                    
                    break
                arr.pop()


        bfs(0,[])
        
        return final