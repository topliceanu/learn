package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	go func() {
		messages <- "some message"
		messages <- "some other message"
	}()

	go func() {
		signals <- false
	}()

	select {
	case msg := <-messages:
		fmt.Println("Recevied messages", msg)
	default:
		fmt.Println("No message received")
	}

	select {
	case messages <- "something stupid":
		fmt.Println("Sent message")
	default:
		fmt.Println("No messages sent")
	}

	select {
	case msg := <-messages:
		fmt.Println("Recevied messages", msg)
	case signal := <-signals:
		fmt.Println("Received signals", signal)
	default:
		fmt.Println("No activity")
	}
}
