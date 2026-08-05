class Solution(object):
    def lcs(self,text1,text2):
        n=len(text1)
        m=len(text2)
        dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
        for ind2 in range(0,m+1):
            dp[0][ind2]=0
        for ind1 in range(0,n+1):
            dp[ind1][0]=0
        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                if text1[ind1-1]==text2[ind2-1]:
                    dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]=max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        return dp[n][m]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n=len(word1)
        m=len(word2)
        l=self.lcs(word1,word2)
        return n+m-(2*l)