/*
We want to build a system which receives a set of urls and reports on their
status code at a give interval.
*/

var urls = []string{
	"http://alexandrutopliceanu.ro",
	"http://musicbits.ro",
	"http://learnscalability.com",
}

type StatusReporter interface {
	Status() int
}

func report(reporters... StatusReporter) {

}

func main() {
	kkk
}
