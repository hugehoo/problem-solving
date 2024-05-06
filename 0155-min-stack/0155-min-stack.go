type MinStack struct {
    stack []int
    min []int
    top int
    
}


func Constructor() MinStack {
    return MinStack{[]int{}, []int{}, -1}
}


func (this *MinStack) Push(val int)  {
    if this.top == -1 {
        this.min = append(this.min, val)
    } else {
        this.min = append(this.min, min(val, (this.min)[this.top]))
    }
    this.stack = append(this.stack, val)
    this.top++
}


func (this *MinStack) Pop()  {
    this.stack = this.stack[:this.top]
    this.min = this.min[:this.top]
    this.top --
    return
}


func (this *MinStack) Top() int {
    return this.stack[this.top]
}


func (this *MinStack) GetMin() int {
    return this.min[this.top]
}

func min(a, b int) int{
    if a < b {
        return a
    }
    return b
}

/**
type MinStack struct {
	stack []int
	min   []int
	top   int
}

func Constructor() MinStack {
	return MinStack{[]int{}, []int{}, -1}
}

func (this *MinStack) Push(val int) {
	if this.top == -1 {
		this.min = append(this.min, val)
	} else {
		this.min = append(this.min, min(val, (this.min)[this.top]))
	}
	this.stack = append(this.stack, val)
	this.top++
}

func (this *MinStack) Pop() {
	this.stack = this.stack[:this.top]
	this.min = this.min[:this.top]
	this.top--
	return
}

func (this *MinStack) Top() int {
	return (this.stack)[this.top]
}

func (this *MinStack) GetMin() int {
	return (this.min)[this.top]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
 */