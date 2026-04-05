class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def format_line(start, end, word_sum, is_last_line):
            num_words = end - start
            total_spaces = maxWidth - word_sum
            
            # Case 1: Last line or only one word in line (Left Justified)
            if is_last_line or num_words == 1:
                # Join with 1 space, then pad the rest on the right
                line = " ".join(words[start:end])
                return line + " " * (maxWidth - len(line))
            
            # Case 2: Fully Justified
            num_gaps = num_words - 1
            base_spacing = total_spaces // num_gaps
            extra_spaces = total_spaces % num_gaps
            
            line = ""
            for i in range(start, end - 1): # Go up to the second to last word
                line += words[i]
                # Every gap gets the base spacing
                # The first 'extra_spaces' gaps get 1 additional space
                current_gap = base_spacing + (1 if i - start < extra_spaces else 0)
                line += " " * current_gap
            
            line += words[end - 1] # Add the last word (no trailing space)
            return line

        justified = []
        pos = 0
        
        while pos < len(words):
            start = pos
            line_weight = 0
            
            # Find how many words fit (Weight + Min Gaps)
            # (pos - start) represents the number of mandatory 1-unit gaps
            while pos < len(words) and line_weight + len(words[pos]) + (pos - start) <= maxWidth:
                line_weight += len(words[pos])
                pos += 1
            
            # Determine if this is the last line
            is_last = (pos == len(words))
            
            # Format using the range [start:pos]
            justified.append(format_line(start, pos, line_weight, is_last))
            
        return justified