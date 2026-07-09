class Solution(object):
    def minDays(self, n):
       
        memo = {}
        
        def dp(n):
            if n <= 1:
                return n
            if n in memo:
                return memo[n]
            
            result = min(
                n % 2 + 1 + dp(n // 2),
                n % 3 + 1 + dp(n // 3)
            )
            memo[n] = result
            return result
        
        return dp(n)