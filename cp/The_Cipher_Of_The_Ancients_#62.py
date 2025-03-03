def lowestCommonSubsequence(s1, s2, m, n, memo):
    
    if m == 0 or n == 0:
        return 0

    if memo[m][n] != -1:
        return memo[m][n]

    if s1[m - 1] == s2[n - 1]:
        memo[m][n] = 1 + lowestCommonSubsequence(s1, s2, m - 1, n - 1, memo)
        return memo[m][n]

    memo[m][n] = max(lowestCommonSubsequence(s1, s2, m, n - 1, memo),
                     lowestCommonSubsequence(s1, s2, m - 1, n, memo))
    
    return memo[m][n]

s1 = input().replace("\"", "")
s2 = input().replace("\"", "")

m = len(s1)
n = len(s2)
memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
print(lowestCommonSubsequence(s1, s2, m, n, memo))