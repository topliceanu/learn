use std::collections::HashMap;

#[derive(PartialEq, Debug)]
pub enum Median {
    // If input array is odd-length, the median is middle element.
    Odd(i32),
    // If input is even-length, the median is the average of the two middle elements.
    Even(f32),
}

#[derive(PartialEq, Debug)]
pub struct MedianAndMode {
    pub median: Median,
    pub mode: i32,
}

pub fn median_and_mode(ints: &[i32]) -> Option<MedianAndMode> {
    let n = ints.len();
    if n == 0 {
        return None;
    }
    let mut ints: Vec<&i32> = ints.iter().collect(); // Copy the vector.
    ints.sort();
    let mut median = Median::Odd(*ints[n / 2]);
    if n.is_multiple_of(2) {
        median = Median::Even((*ints[n / 2 - 1] + *ints[n / 2]) as f32 / 2f32)
    }
    let mut counts: HashMap<i32, i32> = HashMap::new();
    let mut mode: i32 = *ints[0];
    let mut max_count: i32 = 1;
    for i in ints {
        let count = counts.entry(*i).or_insert(0);
        *count += 1;
        if *count > max_count {
            mode = *i;
            max_count = *count;
        }
    }
    Some(MedianAndMode { median, mode })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn median_for_even_input_len() {
        let a = vec![1, 2, 3, 4];
        let res = median_and_mode(&a).unwrap();
        assert_eq!(res.median, Median::Even(2.5));
        assert_eq!(res.mode, 1);
    }
    #[test]
    fn median_for_odd_input_len() {
        let a = vec![1, 2, 3, 4, 5];
        let res = median_and_mode(&a).unwrap();
        assert_eq!(res.median, Median::Odd(3));
        assert_eq!(res.mode, 1);
    }
    #[test]
    fn median_for_unsorted_input() {
        let a = vec![5, 3, 2, 4, 1];
        let res = median_and_mode(&a).unwrap();
        assert_eq!(res.median, Median::Odd(3));
        assert_eq!(res.mode, 1);
    }
    #[test]
    fn mode_for_simple_case() {
        let a = vec![5, 1, 3, 2, 4, 2]; // 1,2,2,3,4,5
        let res = median_and_mode(&a).unwrap();
        assert_eq!(res.median, Median::Even(2.5f32));
        assert_eq!(res.mode, 2);
    }
    #[test]
    fn mode_for_multiple_options() {
        let a = vec![1, 1, 2, 2];
        let res = median_and_mode(&a).unwrap();
        assert_eq!(res.median, Median::Even(1.5f32));
        assert_eq!(res.mode, 1);
    }
    #[test]
    fn median_and_mode_for_empty_input() {
        let a = vec![];
        let res = median_and_mode(&a);
        assert_eq!(res, None);
    }
}

/*
fn to_pig_latin(s: &str) -> String {

}

struct Org {

}

impl Org {
    fn command(&mut self, cmd:&str) {

    }
    fn list(&self, department:&str) -> Vec<&str> {

    }
}
*/
