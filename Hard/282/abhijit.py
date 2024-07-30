class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(cur_idx,cur_res, cur_sum, prev):
            if cur_idx >= len(num):
                if curr_sum == target:
                    res.append("".join(cur_res))
                
                return
            else:
                for i in range(curr_idx, len(num)):
                    cur_str = num[curr_idx: i + 1]
                    cur_num = int(cur_str)
                    if not cur_res:
                        dfs(i + 1, [curr_str], cur_num, cur_num)
                    else:
                        dfs(i + 1, cur_res + ["+"] + [cur_str], cur_sum + cur_num, cur_num)
                        dfs(i + 1, cur_res + ["-"] + [cur_str], cur_sum - cur_num, -cur_num)
        