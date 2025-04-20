class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        def checkDifference(s1,s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count +=1
            return count == 1
        
        graph = {}
        
        
        for i in range(len(wordList)):
            graph[wordList[i]] = []

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if checkDifference(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])  # this makes it undirected

        seen = set()
        def bfs(start):
            nonlocal seen, graph
            q = deque()
            q.append(start)
            count = 0
            while q:
                count += 1
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr == endWord:
                        return count
                    if curr not in seen:
                        for neighbour in graph[curr]:
                            if neighbour not in seen:
                                q.append(neighbour)
                        seen.add(curr)
            return -1

        count = bfs(beginWord)
        if count > 0:
            return count
        return 0
        
                