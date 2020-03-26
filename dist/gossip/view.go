package main

type view map[string]*peerConfig

func newView(configs []*peerConfig) view {
	var (
		v = make(view)
		pc *peerConfig
	)
	for _, pc = range configs {
		v[pc.id] = pc
	}
	return v
}

func (v view) add(pc *peerConfig) bool {
	var exists bool
	if _, exists = v[pc.id]; !exists {
		v[pc.id] = pc
	}
	return exists
}

func (v view) remove(id string) bool {
	_, exists = v[id]
	delete(v, id)
	return exists
}
