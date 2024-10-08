class Solution:
    def check(self, mp, word1, word2):
        i, j = 0, 0
        # Compare character by character until one of the words runs out of characters
        while i < len(word1) and j < len(word2):
            # If word1 has a greater character, return False
            if mp[word1[i]] > mp[word2[j]]:
                return False
            # If word2 has a greater character, return True
            elif mp[word1[i]] < mp[word2[j]]:
                return True
            i += 1
            j += 1
        # If word1 has run out of characters, return True (word1 is less than or equal to word2)
        # If word2 has run out of characters, return False (word1 is greater than word2)
        return len(word1) <= len(word2)
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        # Create a mapping of characters to their positions in the given order
        for i, c in enumerate(order):
            mp[c] = i
        # Iterate over the list of words and compare each consecutive pair using the check function
        for i in range(len(words) - 1):
            if not self.check(mp, words[i], words[i + 1]):
                return False
        # If all pairs are in the correct order, return True
        return True