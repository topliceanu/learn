// See https://exercism.org/tracks/rust/exercises/reverse-string

pub fn reverse(input: &str) -> String {
    let mut reversed: String = String::with_capacity(input.len()); 
    reversed.extend(input.chars().rev()); // TODO: iteration over graphemes is safer.
    reversed
}
