class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hIindex = 0
        sorted_citations = sorted(citations)
        for i in range(len(citations) + 1):
            count = 0
            for n in sorted_citations:
                if n >= i:
                    count += 1

            if count >= i:
                hIndex = i
            else:
                break
        
        return hIndex
            