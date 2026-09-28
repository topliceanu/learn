pub fn encode(source: &str) -> String {
    let source = source.as_bytes();
    let mut out: Vec<char> = vec![];
    let mut index = 0;
    while index < source.len() {
        let (ch, num) = consume_seq(source, index);
        if num != 1 {
            for ch in num_to_chars(num).into_iter() {
                out.push(ch);
            }
        }
        out.push(ch);
        index += num;
    }
    return out.iter().collect();
}

// source  a a b
// index   0 0
// count   1 2
fn consume_seq(source: &[u8], index: usize) -> (char, usize) {
    let ch = source[index];
    let mut count = 1; 
    while index+count < source.len() && ch == source[index+count] {
        count += 1;
    }
    return (ch as char, count);
}

fn num_to_chars(num: usize) -> Vec<char> {
    num.to_string().chars().collect()
}

pub fn decode(source: &str) -> String {
    let mut index: usize = 0;
    let mut output: Vec<char> = vec![];
    let source = source.as_bytes();
    while index < source.len() {
        if let Some(ch) = consume_ch(source, index) {
           output.push(ch);
           index += 1;
        } else if let Some((num, count)) = consume_num(source, index) {
            if let Some(ch) = consume_ch(source, index+count) {
                for _ in 0..num {
                    output.push(ch);
                }
                index += count + 1;
            } else {
                panic!("rle parse error: expected character after number");
            }
        } else {
            panic!("rle parse error: expected character or number");
        }
    }
    return output.iter().collect();
}

fn consume_num(source: &[u8], index: usize) -> Option<(usize, usize)> {
    let mut out: usize = 0;
    let mut i = 0;
    while ('0' as u8) <= source[index+i] && source[index+i] <= ('9' as u8) {
        let digit = (source[index+i] - ('0' as u8)) as usize;
        out = out*10 + digit;
        i += 1;
    }
    if i == 0 { 
        return None;
    }
    return Some((out, i));
}

fn consume_ch(source: &[u8], index: usize) -> Option<char> {
    if ('A' as u8) <= source[index] && source[index] <= ('z' as u8) || source[index] == (' ' as u8) {
        Some(source[index] as char)
    } else {
        None
    }
}

mod tests {
    use crate::run_length_encoding as rle;

    #[test]
    fn encode_empty_string() {
        let input = "";
        let output = rle::encode(input);
        let expected = "";
        assert_eq!(output, expected);
    }
    #[test]
        fn encode_single_characters_only_are_encoded_without_count() {
        let input = "XYZ";
        let output = rle::encode(input);
        let expected = "XYZ";
        assert_eq!(output, expected);
    }
    #[test]
        fn encode_string_with_no_single_characters() {
        let input = "AABBBCCCC";
        let output = rle::encode(input);
        let expected = "2A3B4C";
        assert_eq!(output, expected);
    }
    #[test]
        fn encode_single_characters_mixed_with_repeated_characters() {
        let input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB";
        let output = rle::encode(input);
        let expected = "12WB12W3B24WB";
        assert_eq!(output, expected);
    }
    #[test]
        fn encode_multiple_whitespace_mixed_in_string() {
        let input = "  hsqq qww  ";
        let output = rle::encode(input);
        let expected = "2 hs2q q2w2 ";
        assert_eq!(output, expected);
    }
    #[test]
        fn encode_lowercase_characters() {
        let input = "aabbbcccc";
        let output = rle::encode(input);
        let expected = "2a3b4c";
        assert_eq!(output, expected);
    }
    #[test]
        fn decode_empty_string() {
        let input = "";
        let output = rle::decode(input);
        let expected = "";
        assert_eq!(output, expected);
    }
    #[test]
        fn decode_single_characters_only() {
        let input = "XYZ";
        let output = rle::decode(input);
        let expected = "XYZ";
        assert_eq!(output, expected);
    }
    #[test]
        fn decode_string_with_no_single_characters() {
        let input = "2A3B4C";
        let output = rle::decode(input);
        let expected = "AABBBCCCC";
        assert_eq!(output, expected);
    }
    #[test]
        fn decode_single_characters_with_repeated_characters() {
        let input = "12WB12W3B24WB";
        let output = rle::decode(input);
        let expected = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB";
        assert_eq!(output, expected);
    }
    #[test]
        fn decode_multiple_whitespace_mixed_in_string() {
        let input = "2 hs2q q2w2 ";
        let output = rle::decode(input);
        let expected = "  hsqq qww  ";
        assert_eq!(output, expected);
    }
    #[test]
        fn decode_lowercase_string() {
        let input = "2a3b4c";
        let output = rle::decode(input);
        let expected = "aabbbcccc";
        assert_eq!(output, expected);
    }
    #[test]
        fn consistency_encode_followed_by_decode_gives_original_string() {
        let input = "zzz ZZ  zZ";
        let output = rle::decode(&rle::encode(input));
        let expected = "zzz ZZ  zZ";
        assert_eq!(output, expected);
    }
}