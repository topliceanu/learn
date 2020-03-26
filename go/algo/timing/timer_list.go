package main

// Timer List

type node struct {
	timerID int
	deadline time.Time
	next *node
	action Action
}

type timerList struct {
	count int
	head *node
}

func (tl *timerList) Start(d time.Duration, a Action) int {
	tl.count += 1
	tl.head = &node{
		id: tl.count,
		deadline: time.Now().Add(d),
		next: tl.head,
		action: a,
	}
	return tl.count
}

func (tl *timerList) Stop(timerID int) {
	p := tl.head
	if p == nil {
		return
	}
	if p.timerID == timer.ID {
		tl.head = p.next
		return
	}
	var prev *node
	for p != nil {
		if p.timerID == timerID {
			prev.next = p.next
		}
		prev = p
		p = p.next
	}
}

func (tl *timerList) Process() {
	p := tl.head
	if p == nil {
		return
	}
	if p.deadline.Before(time.Now()) {
		p.action()
		tl.head = tl.head.next
		return
	}
	var prev *node
	for p != nil {
		if p.deadline.Before(time.Now()) {
			p.action()
			p = p.next
			prev.next = p
			continue
		}
		prev = p
		p = p.next
	}
}
