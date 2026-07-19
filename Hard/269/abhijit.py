import string
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        before = {}

        if len(words) == 1:
            # For a single word, just extract its unique characters in order of appearance
            return "".join(dict.fromkeys(words[0]))

        first, second = 0, 1

        while second < len(words):
            f, s = words[first], words[second]
            found = 0
            
            for i in range(max(len(f), len(s))):
                # --- RULE 1: Initialize ANY character we are currently looking at ---
                if i < len(f) and f[i] not in before:
                    before[f[i]] = set()
                if i < len(s) and s[i] not in before:
                    before[s[i]] = set()

                # --- RULE 2: Run your structural checks ---
                if i >= len(s) and found == 0:
                    """
                    the second word is a substring (breaks lexicographic sorting)
                    """
                    print("breaking out:", i, f, s)
                    return ""
                    
                elif i >= len(f) or i >= len(s):
                    """
                    One word ran out of letters. We already initialized the remaining 
                    letters of the longer word above, so we can just move on.
                    """
                    continue
                    
                elif f[i] == s[i]:
                    """
                    characters match, keep moving
                    """
                    continue
                    
                elif found > 0:
                    """
                    We already found our discriminator for these two words. 
                    We don't add order rules for these letters, but they were 
                    already initialized above if they didn't exist!
                    """
                    continue
                    
                else:
                    """
                    found == 0 and f[i] != s[i] -> The discriminator!
                    """
                    # Direct contradiction check
                    if s[i] in before[f[i]]:
                        print("breaking out:",before, i, f, s)
                        return ""

                    found += 1
                    before[s[i]].add(f[i])
            
            first += 1
            second += 1

        print(before)
        # 1. Find all initial nodes with 0 dependencies
        queue = [k for k, deps in before.items() if len(deps) == 0]
        final_string = ""

        # 2. Process the queue until it's empty
        while queue:
            k = queue.pop(0) 
            final_string += k
            
            if k in before:
                del before[k]
                
            for c, deps in before.items():
                if k in deps:
                    deps.remove(k)
                    if len(deps) == 0 and c not in queue:
                        queue.append(c)

        # Since we built 'before' dynamically, its final total size represents 
        # all unique characters we encountered across all words.
        # If there's a cycle, final_string will be shorter than that total.
        return final_string if len(before) == 0 else ""