class Solution(object):
    def solve(self,index,buy,prices,dp):
        if index==len(prices):
            return 0
        if dp[index][buy]!=-1:
            return dp[index][buy]
        if buy==1:
            buyStock=-prices[index]+self.solve(index+1,0,prices,dp)
            notBuy=self.solve(index+1,1,prices,dp)
            profit=max(buyStock,notBuy)
        else:
            sell=prices[index]+self.solve(index+1,1,prices,dp)
            notSell=self.solve(index+1,0,prices,dp)
            profit=max(sell,notSell)
        dp[index][buy]=profit
        return dp[index][buy]
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        dp=[[-1,-1] for _ in range(n)]
        return self.solve(0,1,prices,dp)