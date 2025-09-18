class TaskManager: # heap solution with lazy deletion

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.heap = []

        for userId, taskId, priority in tasks:
            self.tasks[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-1 * priority, -1 * taskId))
      
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-1 * priority, -1 * taskId)) 

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, oldPriority = self.tasks[taskId]
        self.tasks[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-1 * newPriority, -1 * taskId))
        

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, taskId = heapq.heappop(self.heap)
            if (taskId * -1) in self.tasks and self.tasks[-1 * taskId][1] == (-1 * priority):
                return self.tasks[-1 * taskId][0]
            else:
                continue
        return -1
        

from sortedcontainers import SortedList

class TaskManager: # learnt about sortedList
    def __init__(self, tasks):
        self.mp = {}  # taskId -> (userId, priority)
        self.st = SortedList()

        for userId, taskId, priority in tasks:
            self.mp[taskId] = (userId, priority)
            self.st.add((priority, taskId))

    def add(self, userId, taskId, priority):
        self.mp[taskId] = (userId, priority)
        self.st.add((priority, taskId))

    def edit(self, taskId, newPriority):
        userId, oldPriority = self.mp[taskId]
        self.st.remove((oldPriority, taskId))
        self.mp[taskId] = (userId, newPriority)
        self.st.add((newPriority, taskId))

    def rmv(self, taskId):
        userId, priority = self.mp.pop(taskId)
        self.st.remove((priority, taskId))

    def execTop(self):
        if not self.mp:
            return -1
        priority, taskId = self.st.pop()  # O(log n), highest priority
        userId, _ = self.mp.pop(taskId)
        return userId
