class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # arr = [[0] * len(text1) for _ in range(len(text2))]
        m, n = len(text1), len(text2)
        arr = [[0] * (n + 1) for _ in range(m + 1)]

        # 2. Iterate backwards from the end of the strings
        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                
                if text1[x] == text2[y]:
                    # If they match, it's 1 + whatever the best was 
                    # for the REMAINING suffixes (diagonally down-right)
                    arr[x][y] = 1 + arr[x + 1][y + 1]
                else:
                    # If they don't match, the best we can do is the max
                    # of skipping one char in text1 OR one char in text2
                    arr[x][y] = max(arr[x + 1][y], arr[x][y + 1])
        
        return arr[0][0]