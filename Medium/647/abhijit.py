class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        we have n + n/2. start points.
        at each start point we expan out and try to find a string.

        we can safely assume that the palindromes can be made from smaller palindromes like a russian doll.
        so we can only proceed from the start point and expand outwards. 
        if we find a palindrome we can keep expanding until we find a non-palindrome.
        """

        def findPalindromes(start,end):
            count = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
            
            return count

        total_sum = 0
        for i in range(len(s)):
            start = i
            end = i + 1 if i < len(s) - 1 else -1

            odd = findPalindromes(start,start)
            even = 0 if end < 0 else findPalindromes(start,end)
            total_sum = total_sum + odd + even
        
        return total_sum
