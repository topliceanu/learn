use std::cmp::min;

pub fn quick_sort_norec<T: PartialOrd>(xs: &mut [T]) {
    if xs.len() == 0 {
        return
    }
    let mut stack: Vec<(usize, usize)> = vec![];
    stack.push((0, xs.len()-1));
    while let Some((left, right)) = stack.pop() {
        if left == right {
            continue
        }
        if left+1 == right {
            if xs[left] > xs[right] {
                xs.swap(left, right);
            }
            continue 
        }
        let pivot = (left + right) / 2;
        xs.swap(left, pivot);
        let pivot = partition(xs, left, right);
        stack.push((left, pivot));
        stack.push((pivot+1, right));
    }
}

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

// Mergesort produces a new array with the sorted contents of the readonly input array.
// Extra space complexity is O(n). An attempt is made to avoid extra allocations.
// Time complexity is O(nlogn).
// Idea: avoid recursion by splitting the input into increasing larger subarrays (1, 2, 4, 8, ..), sorting them, then merging them with the next subarray.
pub fn merge_sort_norec<T: PartialOrd + Copy>(xs: &mut [T]) {
    let mut out: Vec<T> = vec![];
    let n = xs.len();
    if n <= 1 {
        return
    }
    out = vec!(xs[0]; xs.len()); // Only extra allocation!
    let mut size = 1; // Number of elements in a subarray.
    while size < n { 
        let mut left = 0;
        while left < n - 1 {
            let mid = (left + size).min(n-1); 
            let right = (left + 2*size).min(n);
            merge_sort_merge(xs, out.as_mut_slice(), left, mid, right);
            left += 2*size;
        }
        size *= 2;
    }
}

fn merge_sort_merge<T: PartialOrd+Copy>(xs: &mut [T], out: &mut [T], left: usize, mid: usize, right: usize) {
    let mut i = left;
    let mut j = mid;
    let mut k = 0;
    while i < mid && j < right {
        if xs[i] < xs[j] {
            out[k] = xs[i];
            i += 1;
        } else {
            out[k] = xs[j];
            j += 1;
        }
        k += 1;
    }
    while i < mid {
        out[k] = xs[i];
        (i, k) = (i+1, k+1);
    }
    while j < right {
        out[k] = xs[j];
        (j, k) = (j+1, k+1);
    }
    // Put the sorted elements back in the input array.
    xs[left..right].copy_from_slice(&out[0..k]);
}

pub fn heap_sort<T: PartialOrd+Clone>(xs: &[T]) -> Vec<T>{
    let n = xs.len();
    let mut result= xs.to_vec();
    if n <= 1 {
        return result
    }
    // max-heapify
    for start in (0..n).rev() {
        sift_down(&mut result, start, n)
    }
    // extract the max element to the end
    for end in (1..n).rev() { // n-1, ... 1
        result.swap(0, end); // move largest element to the end
        sift_down(&mut result, 0, end) // shift one of the smallest one back. 
    }
    result
}

fn sift_down<T: PartialOrd>(max_heap: &mut [T], root: usize, end: usize) {
    let mut local_root = root;
    loop {
        let mut max = local_root;
        let (left, right) = (2*local_root+1, 2*local_root+2);
        if left < end && max_heap[left] > max_heap[max] {
            max = left;
        }
        if right < end && max_heap[right] > max_heap[max] {
            max = right
        }
        if max == local_root {
            break
        }
        max_heap.swap(max, local_root);
        local_root = max;
    }
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
            let (mut s1, mut s2, mut s3) = (subject.clone(), subject.clone(), subject.clone());

            //quick_sort(s1.as_mut_slice());
            //assert_eq!(s1, expected);
            
            //quick_sort_norec(s2.as_mut_slice());
            //assert_eq!(s2, expected);

            //merge_sort_norec(s3.as_mut_slice());
            //assert_eq!(s3, expected)

            let output = heap_sort(&subject);
            assert_eq!(output, expected);
        }
    }
}
