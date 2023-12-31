# need to polish solution. Not fully functioning
import string
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_hash = dict.fromkeys(string.printable, None) # of the values we've seen
        largest_substring = None
        if(len(s) == 0):
            return 0
    
    
        for curr_index, char in enumerate(s):
            if char_hash[char] == None:
                char_hash[char] = curr_index + 1
            else:
                if largest_substring == None:
                    largest_substring = curr_index + 1 - char_hash[char]
                else:
                    largest_substring = max(largest_substring, curr_index - char_hash[char])
                    char_hash[char] = curr_index + 1
    
        if largest_substring == None:
            return len(s)
        else:
            return largest_substring
        
