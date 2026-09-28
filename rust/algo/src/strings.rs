use std::{collections::HashMap, hash::{DefaultHasher, Hasher}};

// See https://en.wikipedia.org/wiki/Rabin–Karp_algorithm
pub fn rabin_karp_string_search(needle: &str, haystack: &str) -> bool {
    let (n, m) = (needle.len(), haystack.len());
    if n > m {
        return false;
    }
    let mut hasher = DefaultHasher::new();
    hasher.write(needle.as_bytes());
    let needle_hash = hasher.finish();
    let option = haystack.as_bytes().windows(n).find(|window| {
        let mut hasher = DefaultHasher::new();
        hasher.write(*window);
        return hasher.finish() == needle_hash;
    });
    if let None = option {
        return false;
    } 
    return true;
}

// See https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm
pub fn knutt_morris_pratt_string_search(needle: &str, haystack: &str) -> bool {
    if needle.len() > haystack.len() {
        return false;
    }
    let (needle,haystack)   = (needle.as_bytes(), haystack.as_bytes());
    let (m, n) = (needle.len(), haystack.len());

    // Building the table T: T[i] is the lenght of the longest possible proper initial 
    // segment of needle which is also a segment of the substring ending in needle[i-1].
    let mut T: Vec<i64> = vec![0; m];
    T[0] = -1;
    let mut pos: i64 = 1;
    let mut cnd: i64 = 0;
    while pos < m as i64 {
        if needle[pos as usize] == needle[cnd as usize] {
            T[pos as usize] = T[cnd as usize];
        } else {
            T[pos as usize] = cnd;
            while cnd >= 0 && needle[pos as usize] != needle[cnd as usize] {
                cnd = T[cnd as usize];
            }
        }
        pos += 1;
        cnd += 1;
    }

    let mut j: i64 = 0;
    let mut k: i64 = 0;
    while j < n as i64  {
        if needle[k as usize] == haystack[j as usize] {
            j += 1;
            k += 1;
            if k == m as i64 { // Matched the needle in the haystack.
                return true // Could also return the position of the occurance j-k.
            }
        } else {
            k = T[k as usize];
            if k < 0 {
                j += 1;
                j += 1;
            }
        }
    }
    return false
}

// See https://en.wikipedia.org/wiki/Boyer–Moore_string-search_algorithm
pub fn boyer_moore_string_search(needle: &str, haystack: &str) -> bool {
    todo!()
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_knutt_morris_pratt_string_search() {
        let tests: Vec<(String, String, bool)> = vec![
            ("ABCABCDABABCDABCDABDE".to_string(), "ABCDABD".to_string(), true),
        ];
        for (haystack, needle, expected) in tests {
            let actual = knutt_morris_pratt_string_search(&needle, &haystack);
            assert_eq!(expected, actual, "find {:} in {:}", needle, haystack)
        }
    }
}
