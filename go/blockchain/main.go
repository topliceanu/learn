package main

func main() {
	bc := NewBlockchain()
	defer bc.db.Close()

	cli := &CLI{ bc: bc }
	cli.Run()
}
