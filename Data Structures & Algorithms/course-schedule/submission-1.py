class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS Kahn's

        courseM = defaultdict(list)
        dependency = [0] * numCourses

        for a, b in prerequisites:
            courseM[b].append(a)
            dependency[a] += 1
        
        q = deque([i for i in range(numCourses) if dependency[i] == 0])
        completedCount = 0

        while q:
            prereq = q.popleft()
            completedCount += 1

            for course in courseM[prereq]:
                dependency[course] -= 1
                if dependency[course] == 0:
                    q.append(course)
            
        return completedCount == numCourses            

