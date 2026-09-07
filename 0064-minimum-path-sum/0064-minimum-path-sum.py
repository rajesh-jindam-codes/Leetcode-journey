class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])
        prev=[0]*cols
        for i in range(rows):
            curr=[0]*cols
            for j in range(cols):
                if i==0 and j==0:
                    curr[j]=grid[0][0]
                    continue
                if i==0:
                    up=float('inf')
                else:
                    up=prev[j]
                if j==0:
                    left=float('inf')
                else:
                    left=curr[j-1]
                curr[j]=grid[i][j]+min(up,left)
            prev=curr
        return prev[cols-1]