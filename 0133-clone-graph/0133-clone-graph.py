"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        visited={}
        visited[node]=Node(node.val)
        queue=deque([node])
        while queue:
            curr=queue.popleft()
            for adjNode in curr.neighbors:
                if adjNode not in visited:
                    visited[adjNode]=Node(adjNode.val)
                    queue.append(adjNode)
                visited[curr].neighbors.append(visited[adjNode])
        return visited[node]