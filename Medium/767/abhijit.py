class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        heap = []
        for char in s:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        
        for char, count in counts.items():
            heapq.heappush(heap,(-1 * count, char))
        
        return_str = ""
        while heap:
            curr_most_count, curr_most_char = heapq.heappop(heap)

            while curr_most_count < 0:
                return_str += curr_most_char
                curr_most_count += 1
                
                if len(return_str) > 1 and return_str[-1] == return_str[-2]:
                    # unable to find any othe order of strings that can meet our requirements
                    return ""
                
                if heap:
                    next_most_count, next_char = heapq.heappop(heap)
                    return_str += next_char
                    if next_most_count != -1:
                        heapq.heappush(heap,(next_most_count + 1, next_char))
        
        return return_str
