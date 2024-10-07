class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def checkValidDifference(word1, word2):
            changes = 0
            ptr = 0
            while ptr < len(word1):
                if word1[ptr] != word2[ptr]:
                    changes +=1
                ptr +=1
            return True if changes == 1 else False
        
        min_words = float("inf")
        def dfs(begin,end,currChain,words):
            nonlocal min_words
            print('currentwords',words)
            if begin == end:
                min_words = min(currChain,min_words)
                return 
            
            one_diff = set()

            for word in words:
                if checkValidDifference(begin,word):
                    one_diff.add(word)

            for word in one_diff:
                dfs(word,end,currChain +1, words.difference(one_diff))
            
        if endWord not in wordList:
            return 0
        dfs(beginWord,endWord,1,set(wordList))
        return 0 if min_words == float("inf") else min_words


            
    
            
        