package main

// merged implements Subscription interface by aggregating two subscriptions into one.
type merged struct {
	s1   Subscription
	s2   Subscription
	stop chan struct{}
}

func (m *merged) Updates() <-chan Item {
	out := make(chan Item)
	items1 := m.s1.Updates()
	items2 := m.s2.Updates()
	go func() {
		for {
			select {
			case i1 := <-items1:
				out <- i1
			case i2 := <-items2:
				out <- i2
			case <-m.stop:
				return
			}
		}
	}()
	return out
}

func (m *merged) Close() error {
	err1 := m.s1.Close()
	err2 := m.s2.Close()
	m.stop <- struct{}{}
	if err1 != nil {
		return err1
	}
	return err2
}

// Merges multiple subscriptions to return a single subscription.
func Merge(subs ...Subscription) Subscription {
	if len(subs) == 1 {
		return subs[0]
	} else if len(subs) == 2 {
		return &merged{subs[0], subs[1], make(chan struct{})}
	} else {
		m1 := Merge(subs[:len(subs)/2]...)
		m2 := Merge(subs[len(subs)/2:]...)
		return &merged{m1, m2, make(chan struct{})}
	}
}
