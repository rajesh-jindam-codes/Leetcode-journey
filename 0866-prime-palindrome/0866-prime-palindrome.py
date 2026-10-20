class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPrime(x):
            if x<2:
                return False
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    return False
            return True
        if 8<=n<=11:
            return 11
        x=1
        while True:
            s=str(x)
            palindrome=int(s+s[-2::-1])
            if palindrome>=n and isPrime(palindrome):
                return palindrome
            x+=1
        