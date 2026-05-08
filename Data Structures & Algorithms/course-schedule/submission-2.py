class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # KAHN'S

        courseMap = defaultdict(list)
        dependency = [0] * numCourses

        for a, b in prerequisites:
            courseMap[b].append(a)
            dependency[a] += 1
        
        q = deque([i for i in range(numCourses) if dependency[i] == 0])
        courseCompleted = 0

        while q:
            prereq = q.popleft()
            courseCompleted += 1

            for course in courseMap[prereq]:
                dependency[course] -= 1
                if dependency[course] == 0:
                    q.append(course)
            
        return courseCompleted == numCourses