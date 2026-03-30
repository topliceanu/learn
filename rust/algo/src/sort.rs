// Quicksort: sort the given slice in place. Returns the number of swaps needed.
// See https://en.wikipedia.org/wiki/Quicksort
pub fn quick_sort<T: PartialOrd>(slice: &mut [T]) {
    if slice.len() == 0 {
        return;
    }
    rec_quick_sort(slice, 0, slice.len() - 1);
}

fn rec_quick_sort<T: PartialOrd>(slice: &mut [T], left: usize, incl_right: usize) {
    if left >= incl_right {
        return;
    }
    if left + 1 == incl_right {
        if slice[left] > slice[incl_right] {
            slice.swap(left, incl_right)
        }
        return;
    }
    // Pick a pivot in the unsorted area of the input.
    let pivot = pick_pivot(left, incl_right);
    // Swap the pivot value with the first element in the unsorted array.
    slice.swap(pivot, left);
    // Partition the array around the pivot, which is now in position left.
    // Ie. move all the elements smaller than the pivot to it's left.
    let pivot = partition(slice, left, incl_right);
    // Recurse on the the two subslices.
    rec_quick_sort(slice, left, pivot);
    rec_quick_sort(slice, pivot + 1, incl_right);
}

fn pick_pivot(left: usize, right: usize) -> usize {
    // Random selection of the pivot would be ideal but it requires a third party library.
    (left + right).div_ceil(2)
}

fn partition<T: PartialOrd>(slice: &mut [T], left: usize, incl_right: usize) -> usize {
    // We're assuming that the pivot is on the left most position in the slice.
    let mut new_pivot = left + 1;
    for i in left + 1..incl_right + 1 {
        if slice[i] < slice[left] {
            slice.swap(new_pivot, i);
            new_pivot += 1;
        }
    }
    slice.swap(new_pivot - 1, left);
    return new_pivot - 1;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn smoke_test() {
        let tests: Vec<(Vec<i32>, Vec<i32>)> = vec![
            // Edge cases.
            (vec![], vec![]),                                 // empty.
            (vec![1], vec![1]),                               // one element.
            (vec![2, 1], vec![1, 2]),                         // two elements.
            (vec![6, 5, 4, 3, 2, 1], vec![1, 2, 3, 4, 5, 6]), // even elements.
            (vec![5, 4, 3, 2, 1], vec![1, 2, 3, 4, 5]),       // odd elements.
            (vec![1, 1, 1], vec![1, 1, 1]),                   // same element.
            // Regular cases.
            (vec![3, 8, 2, 5, 1, 4, 7, 6], vec![1, 2, 3, 4, 5, 6, 7, 8]),
            (
                vec![2, 6, 5, 3, 7, 8, 1, 9, 4, 0],
                vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            ),
            (
                vec![4, 6, 5, 3, 7, 8, 1, 9, 2, 0],
                vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            ),
        ];
        for (mut subject, expected) in tests {
            quick_sort(subject.as_mut_slice());
            assert_eq!(subject, expected);
        }
    }
}
