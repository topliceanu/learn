package main

func Index(xs []string, x string) int {
	for i, px := range xs {
		if px == x {
			return i
		}
	}
	return -1
}

func Include(xs []string, x string) bool {
	return Index(xs, x) >= 0
}

func Any(xs []string, p func(string) bool) bool {
	for _, x := range xs {
		if p(x) == true {
			return true
		}
	}
	return false
}

func All(xs []string, p func(string) bool) bool {
	for _, x := range xs {
		if p(x) == false {
			return false
		}
	}
	return true
}

func Filter(xs []string, p func(string) bool) bool {
	var out = make([]string, 0)
	for _, x := range xs {
		if p(x) == true {
			out = append(out, x)
		}
	}
	return out
}

func Map(xs []string, p func(string) string) []string {
	var out = make([]string, len(xs))
	for i, x := range xs {
		out[i] = p(x)
	}
	return out
}
