# -*- coding: utf-8 -*-#
# Name:         516_subSequence
# Author:       ARCHI
# Date:         2020/3/20
# Description:  字符串子序列（最长回文串序列，最长公共子序列）
# -------------------------------------------------------------------------------

def longestPalindromeSubseq(s: str) -> int:
    if not s:
        return 0

    n = len(s)
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        temp = 0  # position dp[i-1][i-2] 一定是0，对应二维数组中主对角线下方那一条线上的值
        dp[i], j = 1, i + 1
        while j < n:
            if s[i] == s[j]:
                aa = dp[j]
                dp[j] = temp + 2
                temp = aa
                # temp, dp[j] = dp[j], temp + 2
            else:
                temp = dp[j]
                dp[j] = max(dp[j-1], dp[j])

            j += 1

    return dp[-1]

if __name__ == "__main__":
    s = "bbbabb"
    print(longestPalindromeSubseq(s))