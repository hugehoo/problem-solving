func uniquePaths(m int, n int) int {
	// Initialize a 2D slice (matrix) with dimensions m x n
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	// Set the number of paths for the first row and first column to 1
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 || j == 0 {
				dp[i][j] = 1
			} else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			}
		}
	}

	// Return the number of unique paths to the bottom-right corner
	return dp[m-1][n-1]
}
