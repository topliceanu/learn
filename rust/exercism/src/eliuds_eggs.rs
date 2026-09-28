// https://exercism.org/tracks/rust/exercises/eliuds-eggs

pub fn egg_count(display_value: u32) -> usize {
    let mut count = 0;
    for i in 0..32 {
        if (display_value >> i) & 1 == 1 {
            count += 1
        }
    }
    count
}

pub fn egg_count_std(display_value: u32) -> usize {
    display_value.count_ones() as usize
}

#[test]
fn test_0_eggs() {
    let input = 0;
    let output = egg_count(input);
    let expected = 0;
    assert_eq!(output, expected);
}
#[test]
fn test_1_egg() {
    let input = 16;
    let output = egg_count(input);
    let expected = 1;
    assert_eq!(output, expected);
}
#[test]
fn test_4_eggs() {
    let input = 89;
    let output = egg_count(input);
    let expected = 4;
    assert_eq!(output, expected);
}
#[test]
fn test_13_eggs() {
    let input = 2_000_000_000;
    let output = egg_count(input);
    let expected = 13;
    assert_eq!(output, expected);
}
