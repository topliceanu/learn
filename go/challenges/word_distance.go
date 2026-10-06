package challenges

// See
// Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
// You can insert, delete, or replace a character any number of times.

func wordDistance(word1, word2 string) uint {
	return 0
}

// OCAML implementation
//let distance w1 w2 =
//	match (w1, w2) with
//	| [], [] -> 0
//	| _::_, [] -> List.length w1
//	| [], _::_ -> List.length w2
//	| x::xs, y::ys ->
//		if x == y then distance xs ys
//		else min (1 + distance xs ys) /*replace x with y*/ (1 + distance xs w2) /*insert x in front of w2*/ (1 + distance w1 ys) /*insert y in front of w1*/
