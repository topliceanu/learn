// See https://exercism.org/tracks/rust/exercises/luhn
// See https://en.wikipedia.org/wiki/Luhn_algorithm

pub fn is_valid(code: &str) -> bool {
    if !code.chars().all(|c| c.is_numeric() || c == ' ') {
        return false
    }
    if code.chars().filter(|c| *c != ' ').count() == 1 {
        return false
    }
    let checksum = code
        .as_bytes()
        .iter()
        .filter(|ch| **ch != b' ')// Remove spaces.
        .rev()
        .map(|ch| { ch - ('0' as u8)}) // Convert characters to the associated numbers by subtracting the ASCII for 0.
        .enumerate()
        .map(|(i, ch)| {
            if i % 2 == 0 {
                return ch
            } 
            if ch * 2 > 9 {
                ch * 2 - 9
            } else {
                ch * 2
            }
        })
        .fold(0i32, |sum, x| sum + (x as i32));
    return checksum % 10 == 0;
}

fn is_valid_no_iterators(code: &str) -> bool {
    let mut sum:i32 = 0;
    let mut double= false;
    let mut len = 0;
    for &ch in code.as_bytes().iter().rev() {
        if ch == b' ' {
            continue
        }
        if !ch.is_ascii_digit() {
            return false
        }
        let mut digit = (ch - b'0') as i32;
        if double {
            digit *= 2;
            if digit > 9 {
                digit -= 9;
            }
        }
        sum += digit;
        len += 1;
        double = !double;
    }
    return len > 1 && sum % 10 == 0
}

#[test]
fn single_digit_strings_can_not_be_valid() {
    assert!(!is_valid("1"));
}
#[test]
fn a_single_zero_is_invalid() {
    assert!(!is_valid("0"));
}
#[test]
fn a_simple_valid_sin_that_remains_valid_if_reversed() {
    assert!(is_valid("059"));
}
#[test]
fn a_simple_valid_sin_that_becomes_invalid_if_reversed() {
    assert!(is_valid("59"));
}
#[test]
fn a_valid_canadian_sin() {
    assert!(is_valid("055 444 285"));
}
#[test]
fn invalid_canadian_sin() {
    assert!(!is_valid("055 444 286"));
}
#[test]
fn invalid_credit_card() {
    assert!(!is_valid("8273 1232 7352 0569"));
}
#[test]
fn invalid_long_number_with_an_even_remainder() {
    assert!(!is_valid("1 2345 6789 1234 5678 9012"));
}
#[test]
fn invalid_long_number_with_a_remainder_divisible_by_5() {
    assert!(!is_valid("1 2345 6789 1234 5678 9013"));
}
#[test]
fn valid_number_with_an_even_number_of_digits() {
    assert!(is_valid("095 245 88"));
}
#[test]
fn valid_number_with_an_odd_number_of_spaces() {
    assert!(is_valid("234 567 891 234"));
}
#[test]
fn valid_strings_with_a_non_digit_added_at_the_end_become_invalid() {
    assert!(!is_valid("059a"));
}
#[test]
fn valid_strings_with_punctuation_included_become_invalid() {
    assert!(!is_valid("055-444-285"));
}
#[test]
fn valid_strings_with_symbols_included_become_invalid() {
    assert!(!is_valid("055# 444$ 285"));
}
#[test]
fn single_zero_with_space_is_invalid() {
    assert!(!is_valid(" 0"));
}
#[test]
fn more_than_a_single_zero_is_valid() {
    assert!(is_valid("0000 0"));
}
#[test]
fn input_digit_9_is_correctly_converted_to_output_digit_9() {
    assert!(is_valid("091"));
}
#[test]
fn very_long_input_is_valid() {
    assert!(is_valid("9999999999 9999999999 9999999999 9999999999"));
}
#[test]
fn valid_luhn_with_an_odd_number_of_digits_and_non_zero_first_digit() {
    assert!(is_valid("109"));
}
#[test]
fn using_ascii_value_for_non_doubled_non_digit_isn_t_allowed() {
    assert!(!is_valid("055b 444 285"));
}
#[test]
fn using_ascii_value_for_doubled_non_digit_isn_t_allowed() {
    assert!(!is_valid(":9"));
}
#[test]
fn non_numeric_non_space_char_in_the_middle_with_a_sum_that_s_divisible_by_10_isn_t_allowed() {
    assert!(!is_valid("59%59"));
}