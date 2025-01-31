package main

import (
	"fmt"
)

func getSum(a int, b int) int {
	for b != 0 {
		carry := (a & b) << 1
		a = a^b
		b = carry
	}
	return a
}

func main() {
	fmt.Println(getSum(1000, 1000))  // 2000
	fmt.Println(getSum(1000, -100))  // 900
	fmt.Println(getSum(2, 3))        // 5
}




