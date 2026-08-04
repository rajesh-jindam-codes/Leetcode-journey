class Solution(object):
    def dfs(self,r,c,index,board,word):
        rows=len(board)
        cols=len(board[0])
        if index==len(word):
            return True
        if (r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[index]) :
            return False
        temp=board[r][c]
        board[r][c]="#"
        found=(
            self.dfs(r+1,c,index+1,board,word) or 
            self.dfs(r-1,c,index+1,board,word) or
            self.dfs(r,c+1,index+1,board,word) or
            self.dfs(r,c-1,index+1,board,word)
        )
        board[r][c]=temp
        return found
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows=len(board)
        cols=len(board[0])
        for i in range(rows):
            for c in range(cols):
                if self.dfs(i,c,0,board,word):
                    return True
        return False