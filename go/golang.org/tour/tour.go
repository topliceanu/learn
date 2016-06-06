package main

import (
	"fmt"
	"io"
	"math"
	"math/cmplx"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"image"
	"image/color"
	"time"
)

func swap(a, b string) (string, string) {
	return b, a
}

// Return values can be named!
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - y
	return // "naked" return, returns x, y
}

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("cannot find square root of negative number: %f", float64(e))
}

// Square root of a number using Newton's function.
func Sqrt(x float64) (numIter int32, t float64, e error) {
	if x < 0 {
		return -1, -1, ErrNegativeSqrt(x)
	}

	var z float64 = 1.0
	for {
		t = z - (z*z-x)/(2*z)
		if x-t*t < 0.001 && x-t*t > -0.001 {
			return numIter, t, nil
		} else {
			numIter += 1
			z = t
		}
	}
}

type Abser interface {
	Abs() float64
}

type Vertex struct {
	X float64
	Y float64
}

// *Vertex is an Abser because it implements "Abs() float64".
func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func generatePic(dx, dy int) (result [][]uint8) {
	result = make([][]uint8, dx)
	for i := range result {
		result[i] = make([]uint8, dy)
		for j := range result[i] {
			result[i][j] = uint8((i * j))
		}
	}
	return result
}

func WordCount(s string) map[string]int {
	counts := make(map[string]int)
	for _, word := range strings.Fields(s) {
		_, alreadySeen := counts[word]
		if alreadySeen == false {
			counts[word] = 1
		} else {
			counts[word] += 1
		}
	}
	return counts
}

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return b
	}
}

// Publishes the fibonacci numbers on a output channel.
func fibonacciRoutine(c, quit chan int) {
	a, b := 0, 1
	for {
		select {
		case c <- a:
			a, b = b, a+b
		case <-quit:
			fmt.Println("Quit Fibonacci Routine")
			return
		}
	}
}

func describe(i interface{}) {
	fmt.Println("(%v, %t)\n", i, i)
}

type I interface {
	M()
}

type T struct {
	S string
}

func (t *T) M() {
	if t == nil {
		fmt.Println("<nil>")
		return
	}
	fmt.Println(t.S)
}

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("%v (%v years old)", p.Name, p.Age)
}

type IPAddr [4]byte

func (ip IPAddr) String() string {
	return fmt.Sprintf("%d.%d.%d.%d", ip[0], ip[1], ip[2], ip[3])
}

func stringToStream(s string) {
	r := strings.NewReader(s)
	b := make([]byte, 8) // creates a new slice of capacity and length 8.
	for {
		n, err := r.Read(b)
		fmt.Printf("n=%d, err=%v, b=%v\n", n, err, b)
		fmt.Printf("read bytes %q\n", b[:n])
		if err == io.EOF {
			break
		}
	}
}

// Create a custom reader which emits an infinite stream of ASCII character 'A'
type MyReader struct{}

func (r MyReader) Read(out []byte) (int, error) {
	out[0] = 'A'
	return 1, nil
}

type rot13Reader struct {
	r io.Reader
}

func (r rot13Reader) Read(p []byte) (n int, err error) {
	n, err = r.r.Read(p)
	for i := 0; i < len(p); i++ {
		if (p[i] >= 'A' && p[i] < 'N') || (p[i] >= 'a' && p[i] < 'n') {
			p[i] += 13
		} else if (p[i] > 'M' && p[i] <= 'Z') || (p[i] > 'm' && p[i] <= 'z') {
			p[i] -= 13
		}
	}
	return n, err
}

type Image struct{
	Width, Height int
	colr uint8
}

func (r Image) Bounds() image.Rectangle {
	return image.Rect(0, 0, r.Width, r.Height)
}

func (r Image) ColorModel() color.Model {
	return color.RGBAModel
}

func (r Image) At(x, y int) color.Color {
	return color.RGBA{r.colr+uint8(x), r.colr+uint8(y), 255, 255}
}

func say(s string) {
	for i := 0; i < 10; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func computeSum(s []int, c chan int) {
	total := 0
	for _, v := range s {
		total += v
	}
	c <- total
}

func distSum(s []int) int {
	c := make(chan int)
	go computeSum(s[:len(s)/2], c)
	go computeSum(s[len(s)/2:], c)
	first, second := <-c, <-c
	return first + second
}

func clockRoutine() {
	tick := time.Tick(100 * time.Millisecond)
	boom := time.After(500 * time.Millisecond)

	for {
		select {
		case <-tick:
			fmt.Println("tick.")
		case <-boom:
			fmt.Println("Boom!")
			return
		default:
			fmt.Println("  .  ")
			time.Sleep(50 * time.Millisecond)
		}
	}
}

func main() {
	fmt.Println("Welcome to the playground!")
	fmt.Println("The time is", time.Now())
	fmt.Println("My favourite number is", rand.Intn(10))
	fmt.Printf("Now you have %g problems\n", math.Sqrt(7))
	fmt.Println(swap("hello", "world"))

	c, java, python := true, false, "no!"
	fmt.Println(c, java, python)

	var (
		ToBe   bool       = false
		MaxInt uint64     = 1<<64 - 1
		z      complex128 = cmplx.Sqrt(-5 + 2i)
	)
	const f = "%T(%v)\n"
	fmt.Printf(f, ToBe, ToBe)
	fmt.Printf(f, MaxInt, MaxInt)
	fmt.Printf(f, z, z)

	var (
		i  int
		f1 float64
		b  bool
		s  string
	)
	fmt.Printf("%v %v %v %q\n", i, f1, b, s)

	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)

	subject := 3.0
	numIter, sqRoot, err := Sqrt(subject)
	expected := math.Sqrt(subject)
	fmt.Printf("sqrt(%v)=%v (after %v iterations) (actual %v) (error %v)\n", subject, sqRoot, numIter, expected, err)

	i, j := 42, 2701
	p := &i
	*p = 12
	fmt.Println("values are", i, j)

	v := Vertex{1, 2}
	q := &v
	q.X = 1e9
	fmt.Printf("Pointer: %v\n", q)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	slice := primes[1:4]
	fmt.Println(primes, slice)

	printSlice(primes[:0])
	printSlice(primes[:4])
	printSlice(primes[2:])
	printSlice([]int{})

	var sl []int
	sl = append(sl, 0, 1)
	printSlice(sl)
	sl = append(sl, 2, 3)
	printSlice(sl)
	sl = append(sl, 4, 5, 6)
	printSlice(sl)

	var m = map[string]Vertex{
		"Bell Labs": Vertex{40, -74},
		"Google":    Vertex{37, -122},
	}
	fmt.Println(m)

	fmt.Println(WordCount("how happy is the blameless vestal's lot"))

	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(pos(i), neg(-2*i))
	}

	fib := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(fib())
	}

	vert := Vertex{3, 4}
	vert.Scale(10)
	fmt.Println("after scaling", vert, vert.Abs())

	var abser Abser
	abser = &vert
	fmt.Println("Calling a method on an interface", abser.Abs())

	var i1 I
	var t1 *T

	i1 = t1
	describe(i1)
	i1.M()

	i1 = &T{"hello"}
	describe(i1)
	i1.M()

	person := Person{"alex", 29}
	fmt.Println(person)

	googleDns := IPAddr{8, 8, 8, 8}
	fmt.Printf("google's dns ip is %v\n", googleDns)

	number, err := strconv.Atoi("42")
	if err != nil {
		fmt.Println("Could not convert number", err)
	} else {
		fmt.Println("Converted integer", number)
	}

	stringToStream("Hello Alexandru Topliceanu")

	src := strings.NewReader("Lbh penpxrq gur pbqr!")
	dest := rot13Reader{src}
	io.Copy(os.Stdout, &dest)

	go say("World!")
	say("hello")

	items:= []int{1,2,3,4,5,6,7,8, 9}
	total := distSum(items)
	fmt.Printf("the sum of %v is %d\n", items, total)

	fibChan := make(chan int, 10)
	quitFibChan := make(chan int, 10)
	go func() {
		for i := 0; i < 30; i++ {
			fmt.Println(<-fibChan)
		}
		quitFibChan <- 0
	}()
	fibonacciRoutine(fibChan, quitFibChan)

	go clockRoutine()
}
