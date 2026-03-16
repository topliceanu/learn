use rust_book::ch8::{median_and_mode, Median};

#[test]
fn test_median_and_mode() {
    let res = median_and_mode(&vec![1,2,3,4,5,6]).unwrap();
    assert_eq!(res.median, Median::Even(3.5f32));
    assert_eq!(res.mode, 1);
}