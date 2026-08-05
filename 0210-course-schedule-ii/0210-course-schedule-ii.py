class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjList=[[] for _ in range(numCourses)]
        indegrees=[0]*numCourses
        for u,v in prerequisites:
            adjList[v].append(u)
            indegrees[u]+=1
        queue=deque()
        result=[]
        for i in range(numCourses):
            if indegrees[i]==0:
                queue.append(i)
        while len(queue)!=0:
            currNode=queue.popleft()
            result.append(currNode)
            for adjNode in adjList[currNode]:
                indegrees[adjNode]-=1
                if indegrees[adjNode]==0:
                    queue.append(adjNode)
        if len(result)==numCourses:
            return result
        return []