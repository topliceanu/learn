// CCI book, ed. 6, chapter 5: Bit manipulation

/* Tricks:
x ^ 0s = x (because XOR 0 preserves bits)
x ^ 1s = -x (because XOR 1 flips bits)
x ^ x = 0s (because XOR produces 0 for identical inputs)

x & 0s = 0s (because AND 0 clears bits)
x & 1s = x (because AND 1 is only 1 when input is 1)
x & x = x (because x AND x = 1 iff x = 1)

x | 0s = x
x | 1s = 1s
x | x = x

2's complement of K = concat(1, 2^N - K)

Operations: (clear with AND, set with OR, -1 is full 1s in 2's complement)
Get bit i in num: (num & (1 << i)) != 0
Set bit i to 1 in num: num | 1 << i
Clear bit i in num: num & (~(1 << i))
Clear msb through i in num: num & ((1 << i) -1)
Clear bits from i to 0 in num: num & (-1 << (i + 1))
Update bit i to value in num: (num & (~(1<<i))) | (value << i)

See: https://graphics.stanford.edu/~seander/bithacks.html
*/

// Problem 5.1:
// Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
// j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
// can assume that the bits j through i have enough space to fit all of M. That is, if
// M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
// example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
pub fn insertion(n: i32, m: i32, i: u8, j: u8) -> i32 {
    if j <= i || i >= 32 || j >= 32 {
        panic!("incorrect input")
    }
    let mask = !(((1 << (j-i+1)) - 1) << i); // 1111111110000011
    println!("{:#b}\n", mask);
    (n & mask) | (m << i)
}

// Problem 5.2:
// Binary to String: Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a double, print
// the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR."
pub fn binary_to_string(x: f64) -> String {
    todo!()
}


#[cfg(test)]
mod tests {
    use super::insertion;

    #[test]
    fn test_insertion() {
        let cases: Vec<(i32, i32, u8, u8, i32)> = vec![
            (0b10000000000, 0b11001, 2, 6, 0b10001100100),
            (0b1111, 0b10, 1, 2, 0b1101),
        ];
        for case in cases.iter() {
            let (n, m, i, j, expected) = *case;
            let actual = insertion(n, m, i, j);
            assert_eq!(format!("{:#b}", expected), format!("{:#b}", actual));
        }
    }
}


