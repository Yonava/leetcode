class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        this is a backtracking problem.
        we start with grab 3 values.  
            - we can't have a trailing zero.
            - we can't have more than 255
        
        at each level we grab 3 and then we recurse to the next index. 
        passing an array down that we append to and we can join with a period
        """

        finalised_ips = []

        def ObtainAllValidIp(curr_index, prev):
            # base case: consumed entire string
            if curr_index == len(s):
                if len(prev) == 4:
                    finalised_ips.append(".".join(prev))
                return

            # prune invalid segment counts
            if len(prev) >= 4:
                return

            # try segments of length 1 to 3
            for length in range(1, 4):
                if curr_index + length > len(s):
                    break

                segment = s[curr_index:curr_index + length]

                # no leading zero unless exactly "0"
                if segment[0] == "0" and length > 1:
                    continue

                # must be <= 255
                if int(segment) > 255:
                    continue

                prev.append(segment)
                ObtainAllValidIp(curr_index + length, prev)
                prev.pop()

        ObtainAllValidIp(0,[])
        return finalised_ips
    

            
