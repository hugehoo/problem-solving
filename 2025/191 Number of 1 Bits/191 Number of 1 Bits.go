package main

import "fmt"


func hammingWeight(n int) int {
    count := 0
    for n != 0 {
        if n&1 == 1 {
            count++
        }
        n = n >> 1
    }
    return count
}

func main() {
	fmt.Println(hammingWeight(7))
}