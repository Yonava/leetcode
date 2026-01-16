class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_l = 0
        abbr_r = 0
        word_i = 0
        
        while abbr_r < len(abbr):
            if abbr[abbr_r].isalpha():
                if abbr_l != abbr_r:
                    jump = abbr[abbr_l: abbr_r]
                    if jump[0] == "0":
                        return False
                    word_i += int(jump)
                    abbr_l = abbr_r
                    if word_i >= len(word) or word[word_i] != abbr[abbr_l]:
                        return False
                abbr_l += 1
                abbr_r += 1
                word_i += 1
            else:
                abbr_r += 1
    
        if abbr_l != abbr_r:
            jump = abbr[abbr_l: abbr_r]
            if jump[0] == "0":
                return False
            word_i += int(jump)
            
        return word_i == len(word)
