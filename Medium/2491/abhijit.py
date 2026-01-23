class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        curr_product = skill[-1] * skill[0]
        goal_sum = skill[-1] + skill[0]
        l,r = 1, len(skill) - 2

        while r > l:
            if skill[l] + skill[r] != goal_sum:
                return -1
            else:
                curr_product += skill[l] * skill[r]
                l += 1
                r -= 1
        
        return curr_product
        