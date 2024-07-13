class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        all_values = []
        for i in range(len(positions)):
            all_values.append((i,positions[i]))
        # sort by positions
        all_values.sort(key = lambda x: x[1])
        for val in all_values:
            i = val[0]
            if len(stack) == 0:
                # first robot to be considered
                stack.append((i,directions[i]))
                continue
            while directions[i] != stack[-1][1] and len(stack) > 0:
                print(stack)
                # only do these calculations if they are approaching each other.
                if directions[i] == "R" and directions[stack[-1][0]] == "L":
                    if positions[i] < positions[stack[-1][0]]:
                        if healths[i] > healths[stack[-1][0]]:
                            healths[stack[-1][0]] = 0
                            healths[i] -= 1
                            stack.pop()
                        elif healths[i] < healths[stack[-1][0]]:
                            healths[i] = 0
                            healths[stack[-1][0]] -= 1
                        elif healths[i] == healths[stack[-1][0]]:
                            healths[i] = 0
                            healths[stack[-1][0]] = 0
                            stack.pop()
                            break
                    else:
                        stack.append((i,directions[i]))
                        break
                else:
                    if positions[i] > positions[stack[-1][0]]:
                        if healths[i] > healths[stack[-1][0]]:
                            healths[stack[-1][0]] = 0
                            healths[i] -= 1
                            stack.pop()
                        elif healths[i] < healths[stack[-1][0]]:
                            healths[i] = 0
                            healths[stack[-1][0]] -= 1
                        elif healths[i] == healths[stack[-1][0]]:
                            healths[i] = 0
                            healths[stack[-1][0]] = 0
                            stack.pop()
                            break
                    else:
                        stack.append((i,directions[i]))
                        break
            if healths[i] != 0:
                stack.append((i,directions[i]))
        result = []
        for val in healths:
            if val != 0:
                result.append(val)
        return result