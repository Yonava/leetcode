from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def hasCycle(course):
            if state[course] == 1:
                # Node is being visited, hence a cycle
                return True
            if state[course] == 2:
                # Node has already been visited, no cycle here
                return False

            # Mark as visiting
            state[course] = 1
            # Traverse its neighbors
            for neighbor in graph[course]:
                if hasCycle(neighbor):
                    return True
            
            # Mark as visited after exploring all neighbors
            state[course] = 2
            return False
        
        # Check for cycles in each course
        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True

"""
from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def hasCycle(course):
            if state[course] == 1:
                # Node is being visited, hence a cycle
                return True
            if state[course] == 2:
                # Node has already been visited, no cycle here
                return False

            # Mark as visiting
            state[course] = 1
            # Traverse its neighbors
            for neighbor in graph[course]:
                if hasCycle(neighbor):
                    return True
            
            # Mark as visited after exploring all neighbors
            state[course] = 2
            return False
        
        # Check for cycles in each course
        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True
"""

"""
Suppose you start DFS from course A. You mark A as VISITING.

From A, you then move to course B (a prerequisite of A). You mark B as VISITING.

Next, you move to course C (a prerequisite of B). You mark C as VISITING.

Now, if C has a prerequisite that leads back to A, you notice that A is marked as VISITING. This indicates a cycle because you’re trying to revisit a node that’s still in the process of being explored, meaning there’s no way to complete all the prerequisites.

If no cycles are found, you backtrack. When backtracking from C, you mark C as VISITED. Then you mark B as VISITED, and finally, A as VISITED.
"""
