package main

import (
	"fmt"
	"time"
)

type Message struct {
	str  string
	wait chan bool
}

func fanIn(input1, input2 <-chan Message) <-chan Message {
	c := make(chan Message)
	go func() {
		for {
			select {
			case m1 := <-input1:
				c <- m1
			case m2 := <-input2:
				c <- m2
			}
		}
	}()
	return c
}

func boring(msg string) <-chan Message {
	c := make(chan Message)
	go func() {
		for i := 0; ; i += 1 {
			waitForIt := make(chan bool)
			c <- Message{fmt.Sprintf("%s %d", msg, i), waitForIt}
			time.Sleep(time.Duration(rand.Intn(1e3)) * time.Millisecond)
			<-waitForIt
		}
	}()
	return c
}

func main() {
	ann := boring("Ann")
	joe := boring("Joe")
	c := fanIn(ann, joe)
	for {
		msg1 := <-c
		fmt.Println(msg1.str)
		msg2 := <-c
		fmt.Println(msg2.str)
		msg1.wait <- true
		msg2.wait <- true
	}
	fmt.Println("You're boring, I'm leaving")

	/*
		joe := boring("Joe")
		timeout := time.After(5 * time.Second)
		for {
			select {
			case m1 := <-joe:
				fmt.Println(m1.str)
				m1.wait<- true
			case <-time.After(100 * time.Millisecond):
				fmt.Println("Too slow to send messages")
				return
			case <-timeout:
				fmt.Println("Finished listening for messages")
				return
			}
		}
	*/
}
