class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        we can keep track of the count of each number.
        we only move r until we have all counts > 1.
        once we build reach that case, we can start removing values from the l position.
        """

        a, b, c = 0, 0, 0 # trackers
        l, r = 0, 0 # window trackers

        count = 0
        while r < len(s):
            if a >= 1 and b >= 1 and c >= 1:
                # reduce the window
                if s[l] == "a":
                    a -= 1
                if s[l] == "b":
                    b -= 1
                if s[l] == "c":
                    c -= 1
                l += 1
                # we must now also account for all other strings that come after this
                count += len(s) - r + 1
            elif s[r] == "a":
                a += 1
                r += 1
            elif s[r] == "b":
                b += 1
                r += 1
            elif s[r] == "c":
                c += 1
                r += 1
        while a >= 1 and b >= 1 and c >= 1:
            # reduce the window
            if s[l] == "a":
                a -= 1
            if s[l] == "b":
                b -= 1
            if s[l] == "c":
                c -= 1
            l += 1
            count += 1

        return count


