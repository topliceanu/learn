// TODO: Add the necessary trait bounds to `min` so that it compiles successfully.
//   Refer to the documentation of the `std::cmp` module for more information on the traits you might need.
//
// Note: there are different trait bounds that'll make the compiler happy, but they come with
// different _semantics_. We'll cover those differences later in the course when we talk about ordered
// collections (e.g. BTreeMap).

use std::cmp::PartialOrd;
use std::fmt::Debug;

/// Return the minimum of two values.
pub fn min<T>(left: T, right: T) -> T
where
    T: PartialOrd + Debug,
{
    if left <= right {
        left
    } else {
        right
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_min() {
        let a = 1;
        let b: i32 = 2;
        let actual = min(a, b);
        let expected = 1;
        assert_eq!(expected, actual);
    }
}
