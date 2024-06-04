class Solution:
    def findNextDiff(self,original,s,lowerBound,upperBound):
        x = lowerBound
        while x <= upperBound:
            if s[x] != original:
                return x
            else:
                x +=1

    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        count = k
        next_pointer = 0
        longest_sub = 0
        while r < len(s):
            print("str parsed l,r", l,r,s[l:r])
            print("k", count)
            if s[l] == s[r]:
                r +=1
            else:
                if count == k:
                    r += 1
                    count -= 1
                elif count > 0:
                    count -= 1
                    r += 1
                else:
                    longest_sub = max(longest_sub, (r-l))
                    print("r",r)
                    l = self.findNextDiff(s[l],s,l,r)
                    # r += 1
                    count = k - (r -l)
        print("str parsed l,r", l,r,s[l:r])
        print("k", count)
        longest_sub = max(longest_sub, (r-l))
        return longest_sub
