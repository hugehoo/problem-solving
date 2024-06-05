func restoreString(s string, indices []int) string {
    
    
    result := make([]byte, len(s))
	for l,index := range indices {
		result[index] = s[l]
	}
	return string(result)
}