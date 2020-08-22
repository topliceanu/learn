package main

var (
	first_ch, second_ch, third_ch, done_ch chan struct{}
)

func init() {
	first_ch = make(chan struct{})
	second_ch = make(chan struct{})
	third_ch = make(chan struct{})
	done_ch = make(chan struct{})
}

func first_fn() {
	fmt.Println("first")
	first_ch<-struct{}{}
	first_ch<-struct{}{}
}

func second_fn() {
	<-first_ch
	fmt.Println("second")
	second_ch<-struct{}{}
}

func third_fn() {
	<-first_ch
	<-second_ch
	fmt.Println("third")
	close(done_ch)
}

func main() {
	go third_fn()
	go second_fn()
	go first_fn()
	<-done_ch
	close(first_ch)
	close(second_ch)
	close(third_ch)
}
