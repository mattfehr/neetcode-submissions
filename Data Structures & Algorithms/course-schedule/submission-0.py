class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        print(adjList)
        
        visited = set() #fully visited nodes that are safe
        path = set()    #nodes in current dfs branch

        def dfs(node):
            if node in visited: 
                return True
            if node in path:
                return False
            
            path.add(node)

            for n in adjList[node]:
                if not dfs(n):
                    return False
            
            #all neighbors safe so its safe
            path.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True
        
