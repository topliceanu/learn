use std::collections::HashSet;

// Problem 1.1: Is Unique
// Implement an algorithm to determine if a string has all unique characters. 
// What if you cannot use additional data structures.
pub fn is_unique(s: &str) -> bool {
    if s.len() == 0 || s.len() == 1 {
        return true;
    }
    let mut s2:Vec<char> = s.chars().collect();
    s2.sort_unstable();
    for i in 0..s2.len()-1 {
        if s2[i] == s2[i+1] {
            return false;
        }
    }
    return true;
}

// more idiomatic rust.
pub fn is_unique2(s: &str) -> bool {
    if s.len() == 0 || s.len() == 1 {
        return true;
    }
    let mut cs: Vec<char> = s.chars().collect();
    cs.sort_unstable();
    cs.windows(2).all(|w| w[0] != w[1])
}

// assumes s contains only ASCII characters
pub fn is_unique3(s: &str) -> bool {
    let mut mem: u8 = 0; // ASCII chars between 68 and 126 so 7 bits would be enough!
    for c in s.as_bytes() {
        let bit = *c - '0' as u8;
        if (mem & (1 << bit)) == 1 {
            return false;
        }
        mem = mem | (1 << bit);
    }
    return true;
}

// Problem 1.2: Check permutation
// Given two strings, write a method to decide if one is a permutation of the other.
pub fn check_permutation(s1: &str, s2: &str) -> bool {
    if s1.len() != s2.len() {
        return false;
    }
    let mut s1 = s1.chars().collect::<Vec<char>>();
    let mut s2 = s2.chars().collect::<Vec<char>>();
    s1.sort_unstable(); 
    s2.sort_unstable();
    s1 == s2
}

// Problem 1.3: URLify: 
// Write a method to replace all spaces in a string with '%20'. You may assume that the string
// has sufficient space at the end to hold the additional characters, and that you are given the "true"
// length of the string. (Note: If implementing in Java, please use a character array so that you can
// perform this operation in place.)
pub fn urlify(s: &str) -> String {
    let mut cs = s.chars().collect::<Vec<char>>();
    let mut count_spaces = cs.iter().filter(|c| **c == ' ').count();
    count_spaces *= 2;
    for i in 0..count_spaces {
        cs.push(' ');
    }
    for i in (0..s.len()).rev() {
        if cs[i] == ' ' {
            count_spaces -= 2;
            let j = i + count_spaces;
            cs[j..j+3].copy_from_slice(&['%', '2', '0']);
        } else {
            let j = i + count_spaces;
            cs[j] = cs[i];
        }
    }
    return cs.into_iter().collect::<String>();
}

pub fn urlify2(s: &str) -> String {
    s[..s.len()].replace(' ', "%20")
}

// Problem 1.4: Palindrome Permutation
// Given a string, write a function to check if it is a permutation of a palindrome. 
// A palindrome is a word or phrase that is the same forwards and backwards. 
// A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
pub fn palindrome_permutation(s: &str) -> bool {
    if s.len() == 0 || s.len() == 1 {
        return true
    }
    let mut cs = s.to_ascii_lowercase().chars().filter(|c| { *c != ' ' }).collect::<Vec<char>>();
    cs.sort_unstable();
    let mut expect_single_char = cs.len() % 2 == 1;
    let mut i = 0;
    while i < cs.len() - 1 {
        if cs[i] == cs[i+1] {
           i += 2;
        } else {
            if expect_single_char {
                i += 1;
                expect_single_char = false;
            } else {
                return false;
            }
        }
    }
    if i == cs.len() - 1 && !expect_single_char {
        return false
    }
    return true
}

// Complexity: O(n) in time and O(1) in space but only for ASCII alphabetic characters.
pub fn palindrome_permutation2(s: &str) -> bool {
    let mut counter:u32 = 0;
    for c in s.chars() {
        if c.is_ascii_alphabetic() {
            let bit = (c.to_ascii_lowercase() as u32) - ('a' as u32);
            counter = counter ^ (1 << bit);
        }
    }
    counter.count_ones() <= 1
}

// Problem 1.5 One Away: 
// There are three types of edits that can be performed on strings: insert a character,
// remove a character, or replace a character. 
// Given two strings, write a function to check if they are one edit (or zero edits) away.
pub fn one_away(s1: &str, s2: &str) -> bool {
    let (shorter, longer) = if s1.len() > s2.len() { (s2, s1) } else { (s1, s2) };
    if longer.len() - shorter.len() > 1 {
        return false;
    }
    let (shorter, longer) = (shorter.chars().collect::<Vec<char>>(), longer.chars().collect::<Vec<char>>());
    if longer.len() == shorter.len() {
        let mut count_differences = 0;
        for i in 0..shorter.len() {
            if shorter[i] != longer[i] {
                count_differences += 1;
                if count_differences > 1 {
                    return false;
                } 
            }
        }
    } else { // shorter.len() + 1 = longer.len()
        for i in 0..shorter.len() {
            if shorter[i] != longer[i] && shorter[i] != longer[i+1] {
                return false
            }
        }
    }
    return true;
}

// Problem 1.6 String Compression: 
// Implement a method to perform basic string compression using the counts of repeated characters. 
// For example, the string aabcccccaaa would become a2blc5a3.
// If the "compressed" string would not become smaller than the original string, your method should return the original string. 
// You can assume the string has only uppercase and lowercase letters (a - z).
pub fn compress(s: &str) -> String {
    if s.len() <= 2 {
        return s.to_string();
    }
    let mut out:Vec<String> = vec![];
    let bytes:&[u8] = s.as_bytes(); 
    let mut i: usize = 0;
    loop {
        let c = bytes[i];
        let mut count = 1;
        let mut j = i+1;
        while j < bytes.len() {
            if c == bytes[j] {
                count += 1;
            } else {
                break
            }
            j += 1;
        }
        out.push((c as char).to_string());
        out.push(count.to_string());
        i += count;
        if i >= bytes.len() {
            break;
        }
    }
    let potential = out.into_iter().collect::<String>();
    if potential.len() < s.len() {
        return potential;
    }
    return s.to_string();
}

// Problem 1.7. Rotate Matrix: 
// Given an image represented by an NxN matrix, where each pixel in the image is 4
// bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
    // 1 2 3 4 5  1 6 1
    // 6 7 8 9 0  2 7 2
    // 1 2 3 4 5  3 8 3
    //            4 9 4
    //            5 0 5

    // (0, 0) -> (0, 2)
    // (0, 1) -> (1, 2)
    // (0, 2) -> (2, 2)
    // (0, 3) -> (3, 2)
    // (0, 4) -> (4, 2)

    // (1, 0) -> (0, 1)
    // (1, 1) -> (1, 1)
    // (1, 2) -> (2, 1)
    // (1, 3) -> (3, 1)
    // (1, 4) -> (4, 1)

    // (2, 0) -> (0, 0)
    // (2, 1) -> (1, 0)
    // (2, 2) -> (2, 0)
    // (2, 3) -> (3, 0)
    // (2, 4) -> (4, 0)

    // N rows x N columns
    // src: row=0..N, col=0..N, 
    // dst: row=src.col, col=N-src.row 
    let n = matrix.len();
    if n == 1 {
        return
    }
    for i in 0..(n/2) {
        for j in i..(n-i-1) {
            let tmp = matrix[i][j];
            matrix[i][j] = matrix[n-1-j][i];
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
            matrix[j][n-1-i] = tmp;
        }
    }
}

// Problem 1.8 Zero Matrix: 
// Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
pub fn zero_matrix(matrix: &mut Vec<Vec<i32>>) {
    let n = matrix.len();
    if n == 0 { 
        return
    }
    let m = matrix[0].len();
    // Identify rows and columns with at least one zero
    let mut rows: HashSet<usize> = HashSet::new();
    let mut cols: HashSet<usize> = HashSet::new();
    for i in 0..n {
        for j in 0..m {
            if matrix[i][j] == 0 {
                rows.insert(i);
                cols.insert(j);
            }
        }
    }
    // Make entire rows/columns 0.
    for i in 0..n {
        for j in 0..m {
            if rows.contains(&i) || cols.contains(&j) {
                matrix[i][j] = 0
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_urlify() {
        let cases: Vec<(String, String)> = vec![
            ("".to_string(), "".to_string()), // empty input
            ("ab".to_string(), "ab".to_string()), // no spaces

            (" ".to_string(), "%20".to_string()), // single space
            ("a b".to_string(), "a%20b".to_string()), // single space
            (" a".to_string(), "%20a".to_string()), // prefix is space
            ("a ".to_string(), "a%20".to_string()), // postfix is space
            
            ("  ".to_string(), "%20%20".to_string()), // single space
            ("a  b".to_string(), "a%20%20b".to_string()), // single space
            ("  a".to_string(), "%20%20a".to_string()), // prefix is space
            ("a  ".to_string(), "a%20%20".to_string()), // postfix is space

            ("  a  ".to_string(), "%20%20a%20%20".to_string()), // postfix and prefix is double space
        ];
        for (input, expected) in cases.into_iter() {
            let actual = urlify(&input);
            assert_eq!(expected, actual, "{:#?}", input);
        }
    }

    #[test]
    fn test_palindrome_permutation() {
        let cases: Vec<(String, bool)> = vec![
            ("".to_string(), true),
            ("a".to_string(), true),
            ("a ".to_string(), true),
            ("ab".to_string(), false),
            ("aba".to_string(), true),
            ("aBa".to_string(), true),
            ("abba".to_string(), true),
            ("AbBa".to_string(), true),
            ("abcba".to_string(), true),
            ("abcdba".to_string(), false),
            ("Tact Coa".to_string(), true),
        ];
        for (input, expected) in cases.into_iter() {
            assert_eq!(expected, palindrome_permutation(&input), "{:?}", input)
        }
    }

    #[test]
    fn test_one_away() {
        let cases: Vec<(String, String, bool)> = vec![
            ("".to_string(), "".to_string(), true),
            ("a".to_string(), "a".to_string(), true),
            ("a".to_string(), "b".to_string(), true),
            ("b".to_string(), "a".to_string(), true),
            ("ab".to_string(), "a".to_string(), true),
            ("ab".to_string(), "abb".to_string(), true),
            ("".to_string(), "aa".to_string(), false),
            ("aa".to_string(), "bb".to_string(), false),

            // Examples from the book.
            ("paie".to_string(), "pie".to_string(), true),
            ("paies".to_string(), "paie".to_string(), true),
            ("paie".to_string(), "baie".to_string(), true),
            ("paie".to_string(), "bake".to_string(), false),
        ];
        for (s1, s2, expected) in cases.into_iter() {
            assert_eq!(expected, one_away(&s1, &s2), "{:?} {:?}", s1, s2);
        }
    }

        #[test]
    fn test_compress() {
        let cases: Vec<(String, String)> = vec![
            ("a".to_string(), "a".to_string()),
            ("aa".to_string(), "aa".to_string()),
            ("aaa".to_string(), "a3".to_string()),
            ("abb".to_string(), "abb".to_string()),
            ("abbb".to_string(), "abbb".to_string()),
            ("abab".to_string(), "abab".to_string()),
            ("aabb".to_string(), "aabb".to_string()),
            ("aaabbbccc".to_string(), "a3b3c3".to_string()),
        ];
        for (input, expected) in cases.into_iter() {
            assert_eq!(expected, compress(&input), "{:?}", input);
        }
    }

    #[test]
    fn test_zero_matrix() {
        let mut cases: Vec<(Vec<Vec<i32>>, Vec<Vec<i32>>)> = vec![
            (vec![vec![1,0,1], vec![1,1,1]], vec![vec![0,0,0], vec![1,0,1]])
        ];
        for (input, expected) in cases.iter_mut() {
            zero_matrix(input);
            assert_eq!(expected, input, "{:?}", input);
        }
    } 
}
