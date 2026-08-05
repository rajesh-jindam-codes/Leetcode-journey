class Solution(object):
    def dfs(self,node,adjList,visited):
        visited[node]=1
        for adjNode in adjList[node]:
            if visited[adjNode]==0:
                self.dfs(adjNode,adjList,visited)
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        adjList=[[] for _ in range(n)]
        for u,v in invocations:
            adjList[u].append(v)
        visited=[0]*n
        self.dfs(k,adjList,visited)
        for u,v in invocations:
            if visited[u]==0 and visited[v]==1:
                return list(range(n))

        ans=[]
        for i in range(n):
            if visited[i]==0:
                ans.append(i)
        return ans