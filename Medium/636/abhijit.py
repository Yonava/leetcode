class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result, stack, prev = [0] * n, deque(), 0

        for log in logs:
            func, state, time = log.split(":")
            func, time = int(func), int(time)
            if state == "start":
                if stack:
                    result[stack[-1]] += time - prev
                stack.append(func)
                prev = time
            else:
                result[stack.pop()] += time - prev + 1
                prev = time + 1


        return result