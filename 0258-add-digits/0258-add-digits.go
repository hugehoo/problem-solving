func addDigits(num int) int {
    for {
        sum := sumDigits(num)
        num = sum
        
        if num < 10 {
            return num
        }
    }
}


func sumDigits(num int) int {
    var sum int
    for num > 0 {
        digit := num % 10
        sum += digit
        num /= 10 
    }
    return sum
}
