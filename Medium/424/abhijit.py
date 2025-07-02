class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      max_length = 0
      frequency_map = {}
      start, end = 0,0 
      # the frequency trackler is  a neat trick where we can quikcly check what is the most frequently appearing character and then calculated k_used (dynamic) instead of the usual static count
      while end < len(s):
        if s[end] not in frequency_map:
          frequency_map[s[end]] = 0

        frequency_map[s[end]] += 1

        while (end - start + 1) -  max(frequency_map.values()) > k:
          if frequency_map[s[start]] == 1:
            del frequency_map[s[start]] 
          else:
            frequency_map[ss[start]] -= 1

          start += 1

        end += 1
      
        max_length = max(max_length, end - start)
      return max_length 
