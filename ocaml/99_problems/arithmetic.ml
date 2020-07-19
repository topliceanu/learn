(* Arithmetic *)

(* 31. Determine whether a given integer number is prime. (medium)
 * val is_prime : int -> bool
 **)
let is_prime n =
  let rec range left right =
    if left = right then [right]
    else left :: range (left + 1) right

  in let rec aux n = function
    | [] -> true
    | x :: xs ->
        if n mod x = 0 then false
        else aux n xs

  in aux n (range 2 (n / 2))

(* this version does not use the extra list *)
let is_prime_theirs n =
  let rec is_not_divisor n m =
    if m * m > n then true
    else
      if n mod m = 0 then false
      else is_not_divisor n (m + 1)
  in
    if n = 1 then true
    else is_not_divisor n 2

(* 32. Determine the greatest common divisor of two positive integer
 * numbers. (medium) Use Euclid's algorithm.
 * val common_denom : int -> int -> bool
 **)
let rec common_denom a b =
  if b = 0 then a
  else common_denom b (a mod b)

(* 33. Determine whether two positive integer numbers are coprime. (easy)
 * Two numbers are coprime if their greatest common divisor equals 1.
 * val coprime : int -> int -> bool
 **)
let coprime a b =
  (common_denom a b) = 1

(* 34. Calculate Euler's totient function φ(m). (medium)
 * Euler's so-called totient function φ(m) is defined as the number of positive
 * integers r (1 ≤ r < m) that are coprime to m. We let φ(1) = 1.
 * Find out what the value of φ(m) is if m is a prime number. Euler's totient
 * function plays an important role in one of the most widely used public key
 * cryptography methods (RSA).
 * In this exercise you should use the most primitive method to calculate this
 * function (there are smarter ways that we shall discuss later).
 *
 * val totient : int -> int
 **)
let totient m =
  let rec totient_rec i m =
    if m = 1 then 1
    else if i = m then 0
    else if coprime i m then 1 + totient_rec (i + 1) m
    else totient_rec (i + 1) m
  in totient_rec 1 m

(* 35. Determine the prime factors of a given positive integer. (medium)
 * Construct a flat list containing the prime factors in ascending order.
 * var factors : int -> int list
 **)
let factors n =
  let rec aux d n =
    if n = 1 then []
    else if n mod d = 0 then d :: aux d (n / d)
    else aux (d + 1) n
  in aux 2 n

(* 36. Determine the prime factors of a given positive integer (2). (medium)
 * Construct a list containing the prime factors and their multiplicity.
 * Hint: The problem is similar to problem Run-length encoding of a list
 * (direct solution).
 * val factors_pow : int -> (int * int) list
 * FIXME does not work all the time, eg factors_pow 12031
 **)
let factors_pow n =
  let rec collect acc = function
    | [] -> []
    | x :: [] -> [(x, acc + 1)]
    | x :: y :: rest ->
      if x <> y then (x, acc + 1) :: collect 0 (y :: rest)
      else collect (acc + 1) (y :: rest)
  in let fact = factors n
  in collect 0 fact

(* 37. Calculate Euler's totient function φ(m) (improved). (medium).
 * See problem "Calculate Euler's totient function φ(m)" for the definition
 * of Euler's totient function. If the list of the prime factors of a number
 * m is known in the form of the previous problem then the function phi(m)
 * can be efficiently calculated as follows
 *
 * Let [(p1, m1); (p2, m2); (p3, m3); ...] be the list of prime factors
 * (and their multiplicities) of a given number m.
 * Then φ(m) can be calculated with the following formula:
 * φ(m) = (p1 - 1) × p1^(m1 - 1) × (p2 - 1) × p2^(m2 - 1) × (p3 - 1) × p3^(m3 - 1) × ...
 *
 * val phi_improved : int -> int
 **)
let phi_improved n =
  let rec pow a b =
    if b = 0 then 1 else a * pow a (b - 1)
  in let rec phi_rec = function
    | [] -> 1
    | (p, m) :: tl -> (p - 1) * (pow p  (m - 1)) * (phi_rec tl)
  in phi_rec (factors_pow n)

(* 38. Compare the two methods of calculating Euler's totient function. (easy)
 * Use the solutions of problems "Calculate Euler's totient function φ(m)" and
 * "Calculate Euler's totient function φ(m) (improved)" to compare the algorithms.
 * Take the number of logical inferences as a measure for efficiency.
 * Try to calculate φ(10090) as an example.
 **)
let timeit f arg =
  let t0 = Unix.gettimeofday() in
  ignore (f arg);
  let t1 = Unix.gettimeofday() in
  t1 -.t0

(* 39. A list of prime numbers. (easy)
 * Given a range of integers by its lower and upper limit, construct a list
 * of all prime numbers in that range.
 *
 * val all_primes : int -> int -> int list
 **)
let all_primes left right =
  let rec is_prime_aux n d =
    if d > n / 2 then true
    else if n mod d == 0 then false
    else is_prime_aux n (d+1)
  in let rec all_primes_aux l r =
    if l > r then []
    else if is_prime_aux l 2 then l :: all_primes_aux (l+1) r
    else all_primes_aux (l+1) r
  in all_primes_aux left right

(* 40. 40. Goldbach's conjecture. (medium)
 * Goldbach's conjecture says that every positive even number greater than 2 is
 * the sum of two prime numbers. Example: 28 = 5 + 23.
 * It is one of the most famous facts in number theory that has not been proved
 * to be correct in the general case. It has been numerically confirmed up to
 * very large numbers. Write a function to find the two prime numbers that
 * sum up to a given even integer.
 * val goldbach : int -> int * int option
 **)
let goldbach n =
  let rec is_prime_aux n d =
    if d > n / 2 then true
    else if n mod d == 0 then false
    else is_prime_aux n (d+1)
  in let rec goldbach_aux p n =
    if (is_prime_aux p 2) && (is_prime_aux (n-p) 2) then Some (p, n-p)
    else goldbach_aux (p+1) n
  in goldbach_aux 2 n

(* 41. A list of Goldbach compositions. (medium)
 * Given a range of integers by its lower and upper limit,
 * print a list of all even numbers and their Goldbach composition.
 * In most cases, if an even number is written as the sum of two prime numbers,
 * one of them is very small. Very rarely, the primes are both bigger than say 50.
 * Try to find out how many such cases there are in the range 2..3000.
 * val goldbach_list : int -> int -> (int * (int * int))
 **)
let goldbach_list low high =
  let rec goldbach_list_aux l h =
    if l > h then []
    else if l mod 2 != 0 then goldbach_list_aux (l+1) h
    else (l, goldbach l) :: goldbach_list_aux (l+2) h
  in goldbach_list_aux low high

(* val goldbach_limit : int -> int -> int -> (int * (int * int)) *)
let goldbach_limit low high thresh =
  let max_aux a b =
    if a >= b then a
    else b
  in let rec goldbach_limit_aux l h =
    if l > h then []
    else if l mod 2 != 0 then goldbach_limit_aux (l+1) h
    else
      (match goldbach l with
        | None -> goldbach_limit_aux (l+2) h
        | Some (p1, p2) ->
          if p1 > thresh && p2 > thresh then (l, (p1, p2)) :: goldbach_limit_aux (l+2) h
          else goldbach_limit_aux (l+2) h)
  in goldbach_limit_aux (max_aux low thresh) (max_aux thresh high)
