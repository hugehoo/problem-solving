import "strconv"

func isPalindrome(x int) bool {
	strNumber := strconv.Itoa(x)
	lenNumber := len(strNumber)
	for idx, letter := range strNumber {
		it, _ := strconv.Atoi(string(letter))
		u := strNumber[lenNumber-idx-1]
		if strconv.Itoa(it) != string(u) {
			return false
		}
	}
	return true
}
