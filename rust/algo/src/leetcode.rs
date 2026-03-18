// Problem 34. See https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// Find first and last position of element in sorted array.

pub fn first_and_last_pos<T: PartialOrd>(sorted: &[T], target: &T) -> (i32, i32) {
    if sorted.len() == 0 {
        return (-1, -1);
    }
    let first = find_first(sorted, target, 0, sorted.len()-1);
    let last = find_last(sorted, target, 0, sorted.len()-1);
    return (first, last);
}

fn find_first<T: PartialOrd>(sorted: &[T], target: &T, left: usize, right: usize) -> i32 {
    if left == right {
        if sorted[left] == *target {
            return left as i32;
        }
        return -1;
    } 
    let mid = (left+right).div_ceil(2);
    if sorted[mid] == *target {
        let potential_first = find_first(sorted, target, left, mid-1);
        if potential_first == -1 {
            return mid as i32
        } else {
            return potential_first
        }
    } else if sorted[mid] > *target {
        return find_first(sorted, target, left,mid-1);
    } else { // sorted[mid] < *target
        return find_first(sorted, target, mid+1, right);
    }
}


fn find_last<T: PartialOrd>(sorted: &[T], target: &T, left: usize, right: usize) -> i32 {
    if left > right {
        return -1;
    }
    if left == right {
        if sorted[left] == *target {
            return left as i32;
        }
        return -1;
    } 
    let mid = (left+right).div_ceil(2);
    if sorted[mid] == *target {
        let potential_last= find_last(sorted, target, mid+1, right);
        if potential_last == -1 {
            return mid as i32
        } else {
            return potential_last
        }
    } else if sorted[mid] > *target {
        return find_last(sorted, target, left,mid-1);
    } else { // sorted[mid] < *target
        return find_last(sorted, target, mid+1, right);
    }
}

#[cfg(test)]
mod tests {
    use crate::leetcode::first_and_last_pos;

    #[test]
    fn smoke_test() {
        let cases: Vec<(Vec<i32>, i32, i32, i32)> = vec![
            (vec![5,7,7,8,8,10], 8, 3, 4),
            (vec![5,7,7,8,8,10], 6, -1, -1),
            // Edge cases.
            (vec![], 5, -1, -1),
            (vec![1], 1, 0, 0),
            (vec![1], 2, -1, -1),
            (vec![1,2], 2, 1, 1),
        ];
        for (sorted, target, expected_first, expected_last) in cases {
            let (first, last) = first_and_last_pos(&sorted, &target);
            assert_eq!(first, expected_first, "vec={sorted:?} target={target}");
            assert_eq!(last, expected_last, "vec={sorted:?} target={target}");
        }
    }
}