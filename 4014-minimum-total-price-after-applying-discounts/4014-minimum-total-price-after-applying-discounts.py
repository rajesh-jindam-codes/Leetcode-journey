class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        total=0
        for i in range(len(prices)):
            if i<len(discounts):
                total+=prices[i]*(100-discounts[i])/100.0
            else:
                total+=prices[i]
        return total