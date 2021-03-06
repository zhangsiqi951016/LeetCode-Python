class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        max_dist = 0

        """
            先找公共子序列
        """
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                max_dist = max(max_dist, dp[i][j])

        """
            返回 两个词的长度和 - 公共子序列的长度
        """
        return len(word1) + len(word2) - 2 * max_dist