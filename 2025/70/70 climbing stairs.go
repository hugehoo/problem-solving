package main

import "fmt"



func climbStairs(n int) int {
	// 1, 2
	dp := make([]int, n + 1)
	if n == 1  || n == 2 {
		return n
	}
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2
	
	for i := 3; i <= n ; i++ {
		dp[i] = dp[i - 1] + dp[i - 2]
	}


	return dp[n]
}

func main() {
	fmt.Println(climbStairs(10))
}