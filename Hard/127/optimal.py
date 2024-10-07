from collections import deque
from typing import List, Set

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Early exit if endWord is not in wordList
        if endWord not in wordList:
            return 0
        
        # Use a set for faster lookup
        wordSet = set(wordList)
        
        # Queue for BFS: (currentWord, currentChainLength)
        queue = deque([(beginWord, 1)])
        
        while queue:
            currentWord, length = queue.popleft()
            
            # If we reach the endWord, return the current path length
            if currentWord == endWord:
                return length
            
            # Explore all possible one-letter transformations
            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = currentWord[:i] + c + currentWord[i+1:]
                    if nextWord in wordSet:
                        # Add nextWord to the queue and mark it as visited by removing it from wordSet
                        queue.append((nextWord, length + 1))
                        wordSet.remove(nextWord)
        
        # If no transformation sequence is found
        return 0
