class Solution:
    def waysToReachStair(self, k: int) -> int:
        n = int(log2(k+1))+4
        dp = [[[0]*2 for _ in range(n+1)] for _ in range(n)]
        for i in range(n-1, -1, -1): 
            for j in range(i+1, -1, -1): 
                x = pow(2, i)-j
                if x > k+1: dp[i][j][0] = dp[i][j][1] = 0 
                else: 
                    if x == k: dp[i+1][j][0] += 1
                    dp[i][j][0] = dp[i][j][1] = dp[i+1][j][0]
                    if x: dp[i][j][0] += dp[i][j+1][1]
        return dp[0][0][0]
