import itertools
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_possible = ["".join(seq) for seq in itertools.product("()", repeat=n)]
        print(all_possible)
        parens = set()
        for permutation in all_possible:
            str_pointer = 0
            return_str = ""
            currStack = []
            while str_pointer < len(permutation):
                if len(currStack) == 0:
                    currStack.append(permutation[str_pointer])
                    str_pointer += 1
                else:
                    if permutation[str_pointer] != currStack[-1]:
                        temp_str = ""
                        while len(currStack) != 0:
                            temp_str = "(" + temp_str + ")"
                            currStack.pop()
                        return_str = return_str + temp_str
                    else:
                        currStack.append(permutation[str_pointer])
                        str_pointer += 1

            if len(currStack) != 0:
                temp_str = ""
                while len(currStack) != 0:
                    temp_str = "(" + temp_str + ")"
                    currStack.pop()
                return_str = return_str + temp_str

            print(f"working with {permutation} and obtained {return_str}")
            parens.add(return_str)
        return parens
        
''' comeback after exploring backtracking a little more'''