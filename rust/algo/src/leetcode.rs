use std::fmt::Binary;

// Problem 4. Median of two sorted arrays in O(log (m+n))
// See https://leetcode.com/problems/median-of-two-sorted-arrays/description/
pub fn median(first: &[i32], second: &[i32]) -> f64 {
    if first.len() == 0 && second.len() == 0 {
        return 0.0
    }
    let n = (first.len() + second.len()) as i64 ;
    if n % 2 == 1 { 
        return order(first, second, (n-1)/2) as f64;
    } else {
        return (order(first, second, (n-1)/2) + order(first, second, n/2 )) as f64 / 2.0
    }
}

fn order(first: &[i32], second: &[i32], k: i64) -> i32 {
    // Obs: the output median is somewhere between the medians of the two arrays in the merged sorted array.
    // Obs: the median of the merged sorted array is in position (len(first) + len(second))/2. I need to find the element with that position.

    let (mut a_start, mut a_end, mut b_start, mut b_end) = (0, first.len() as i64 -1, 0, second.len() as i64 -1);
    loop {
        if a_start > a_end {
            return second[(k-a_start) as usize];
        }
        if b_start > b_end {
            return first[(k - b_start) as usize];
        }
        let (a_index, b_index) = ((a_start + a_end) / 2, (b_start + b_end) / 2);
        let (a_value, b_value) = (first[a_index as usize], second[b_index as usize]);
        if a_index + b_index < k {
            if a_value > b_value { 
                b_start = b_index + 1;
            } else { 
                a_start = a_index + 1;
            }
        } else {
            if a_value > b_value { 
                a_end = a_index - 1;
            } else { 
                b_end = b_index - 1;
            }
        }
    }
}


// Problem 7. Reverse integer. 
// See https://leetcode.com/problems/reverse-integer/description/
pub fn reverse(x: i32) -> i32 {
    let s:String = (x).to_string();
    let mut cs = s.chars();
    let first = match cs.next() {
        None => return 0,
        Some(first) => first,
    };
    let mut output = cs.rev().collect::<Vec<char>>();
    if first == '-' {
        output.insert(0, first);
    } else {
        output.push(first);
    }
    let output = output.iter().collect::<String>().parse::<i32>();
    if let Ok(reverse) = output {
        return reverse
    }
    return 0;
}

// This is a version improved by an LLM using just mathematical operations.
fn reverse_improved(x:i32) -> i32 {
    let mut rev: i32 = 0;
    let mut n = x;
    while n != 0 {
        let digit = n % 10;
        n = n / 10;
        if rev > i32::MAX/10 || (rev == i32::MAX/10 && digit > 7) || rev < i32::MIN/10 || (rev == i32::MIN/10 && digit < -8) {
            return 0
        }
        rev = rev * 10 + digit;
    }
    return rev;
}

// Problem 10. Regular Expression Matching
// See https://leetcode.com/problems/regular-expression-matching/description/
pub fn is_match(s: String, p: String) -> bool {
    // Plan:
    // 1. parse the regular expression into a list of matchers: (Instead of a list, we can have a tree, traversal is DF)
    // - match character x once -> x
    // - match character x zero or more time -> x*
    // - match any character once -> .
    // - match any character zero or more times -> .*
    // 2. each matcher takes a string and output bool (is or is not a match) + the rest of the string, (is_match:bool, rest:&[str])
    // - apply recursive matching for the * pattern: ie. build a set of rest values then iterate the rest of the pattern over it: (is_match:bool, rests: Vec<&[str]>)

    // Tests:
    //"aaaaab", ".*ab"
    //"aaaaab", "a*ab"
    let pattern = Pattern::parse(&p) ;
    let (is_match, rests) = pattern.apply(&s);
    is_match && rests.len() == 0
}

enum Pattern {
    Single(char),
    ZeroOrMultiple(Box<Pattern>),
    Any,
    And(Box<Pattern>, Box<Pattern>),
    End,
}

impl Pattern {
    fn parse(input: &str) -> Self {
        return Pattern::End
    }

    fn apply(&self, input: &str) -> (bool, Vec<&str>) {
        (true, vec![])
    }
}

// Problem 16: 3Sum closest
// Source: https://leetcode.com/problems/3sum-closest/description/
pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
    let mut closest= 0;
    let n = nums.len();
    for i in 0..n {
        for j in 0..n {
            for k in 0..n {
                if i == j && j == k {
                    continue
                } 
                let proposal = nums[i] + nums[j] + nums[k];
                if (proposal - target).abs() < (closest - target).abs() {
                    closest = proposal;
                }
            }
        }
    }
    return closest;
}

// Reduce the O(n^3) to O(n^2*logn) by sorting a copy of the input and using it to search for closest to target-nums[i]-nums[j].
fn three_sum_closest2(nums: Vec<i32>, target: i32) -> i32 {
    let n = nums.len();
    if n <= 3 {
        return nums.iter().sum()
    }
    let mut sorted = nums.clone();
    for i in 1..n-1 {
        
    }
    sorted.sort_unstable();    
    
    return 0
}

// Reduce the complexity to O(n^2) by precomputing the sum of all distinct pairs in nums.
// Then, for each element in the array, finding the pair whose sum added to it is the closest to target.
fn three_sum_closest3(nums: Vec<i32>, target: i32) -> i32 {
    // Precompute the sum of all distinct pairs and sort this list.
    let sums: Vec<i32> = vec![];
    let pairs: Vec<(usize, usize)> = vec![];
    // TODO: compute them. O(n^2)
    let mut diff = 0;
    for i in 0..nums.len() {
        let current = nums[i];
        let zero_diff = target-current;
        let res = sums.binary_search(&zero_diff);
        let (j, k) = match res {
            Ok(t) => pairs[t],
            Err(t) => if t >= pairs.len() { pairs[t-1] } else { pairs[t] },
        };
        //j-1, j, j+1, j>0, j<n-1, j!=i, j!=k
        //k-1, k, k+1, k>0, k<n-1, k!=i
    }
    return target + diff;
}

// Problem 34. Find first and last position of element in sorted array.
// See https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
pub fn first_and_last_pos<T: PartialOrd>(sorted: &[T], target: &T) -> (i32, i32) {
    if sorted.len() == 0 {
        return (-1, -1);
    }
    let first = find_first(sorted, target, 0, sorted.len() - 1);
    let last = find_last(sorted, target, 0, sorted.len() - 1);
    return (first, last);
}

fn find_first<T: PartialOrd>(sorted: &[T], target: &T, left: usize, right: usize) -> i32 {
    if left > right {
        return -1;
    }
    if left == right {
        if sorted[left] == *target {
            return left as i32;
        }
        return -1;
    }
    let mid = (left + right).div_ceil(2);
    if sorted[mid] == *target {
        let potential_first = find_first(sorted, target, left, mid - 1);
        if potential_first == -1 {
            return mid as i32;
        } else {
            return potential_first;
        }
    } else if sorted[mid] > *target {
        return find_first(sorted, target, left, mid - 1);
    } else {
        // sorted[mid] < *target
        return find_first(sorted, target, mid + 1, right);
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
    let mid = (left + right).div_ceil(2);
    if sorted[mid] == *target {
        let potential_last = find_last(sorted, target, mid + 1, right);
        if potential_last == -1 {
            return mid as i32;
        } else {
            return potential_last;
        }
    } else if sorted[mid] > *target {
        return find_last(sorted, target, left, mid - 1);
    } else {
        // sorted[mid] < *target
        return find_last(sorted, target, mid + 1, right);
    }
}

// Problem 42: Trapping rain water: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
// See https://leetcode.com/problems/trapping-rain-water/
pub fn trapping_rain_water(height: Vec<i32>) -> i32 {
    if height.is_empty() {
        return 0;
    }
    let mut left = 0;
    let mut right = height.len() - 1;
    let mut left_max = 0;
    let mut right_max = 0;
    let mut water = 0;

    while left < right {
        if height[left] < height[right] {
            if height[left] >= left_max {
                left_max = height[left];
            } else {
                water += left_max - height[left];
            }
            left += 1;
        } else {
            if height[right] >= right_max {
                right_max = height[right];
            } else {
                water += right_max - height[right];
            }
            right -= 1;
        }
    }
    return water
}

// same as above but precomputes arrays of maxima on left and right side for each index in the input.
fn trapping_rain_water2(height: &[i32]) -> i32 {
    if height.is_empty() {
        return 0;
    }
    let n = height.len();
    let mut left_max = vec![0; n];
    let mut right_max = vec![0; n];
    // Pass 1: Build left maximums
    let mut max = 0;
    for i in 0..n {
        max = max.max(height[i]);
        left_max[i] = max;
    }
    // Pass 2: Build right maximums
    max = 0;
    for i in (0..n).rev() {
        max = max.max(height[i]);
        right_max[i] = max;
    }
    // Pass 3: Calculate trapped water
    let mut water = 0;
    for i in 0..n {
        water += std::cmp::min(left_max[i], right_max[i]) - height[i];
    }
    return water
} 

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_median() {
        let cases: Vec<(Vec<i32>, Vec<i32>, f64)> = vec![
            (vec![], vec![], 0.0),
            (vec![1], vec![], 1.0),
            (vec![], vec![1], 1.0),
            (vec![2], vec![1], 1.5),
            (vec![1, 2], vec![3, 4], 2.5),
            (vec![1, 3], vec![2], 2.0),
            (vec![2], vec![1, 3], 2.0),
        ];
        for (first, second, expected) in cases {
            let actual = median(&first, &second);
            assert_eq!(expected, actual, "Given first={:?} and second={:?}", first, second)
        }
    }

    #[test]
    fn test_reverse() {
        let cases: Vec<(i32, i32)> = vec![
            (0, 0),
            (10, 1),
            (120, 21),
            (1000000000, 1),
            (123, 321),
            (-123, -321),
            (-1000000000, -1),
            (i32::MAX, 0),
            (i32::MIN, 0),
        ];
        for (input, expected) in cases {
            let actual = reverse(input);
            assert_eq!(expected, actual);
        }
    }

    #[test]
    #[ignore]
    fn test_is_match() {
        let cases: Vec<(String, String, bool)> = vec![
            ("ab".to_string(), ".*".to_string(), true),
            ("aab".to_string(), "c*a*b".to_string(), true),
            ("mississippi".to_string(), "mis*is*p*.".to_string(), false),
            ("aab".to_string(), "c*a*b".to_string(), true),
            ("ab".to_string(), ".*c".to_string(), true),
        ];
        for (input, pattern, expected) in cases {
            let actual = is_match(input.clone(), pattern.clone());
            assert_eq!(expected, actual, "input={:} pattern={:}", input, pattern)
        }
    }

    #[test]
    #[ignore]
    fn test_three_sum_closest() {
        let cases: Vec<(Vec<i32>, i32, i32)> = vec![
            (vec![-1,2,1,-4], 2, 2),
            (vec![-1,-1,2,4], 1, 0), // or 0.
            (vec![0,0,0], 1, 0),
            (vec![10,20,30,40,50,60,70,80,90], 1, 60),
            (vec![1,1,1,0], -100, 2),
            (vec![4,0,5,-5,3,3,0,-4,-5], -2, -2),
        ];
        for (input, target, expected) in cases {
            let actual = three_sum_closest2(input.clone(), target);
            assert_eq!(expected, actual, "input={:?} target={:}", input, target)
        }
    }

    #[test]
    fn test_first_and_last_pos() {
        let cases: Vec<(Vec<i32>, i32, i32, i32)> = vec![
            (vec![5, 7, 7, 8, 8, 10], 8, 3, 4),
            (vec![5, 7, 7, 8, 8, 10], 6, -1, -1),
            // Edge cases.
            (vec![], 5, -1, -1),
            (vec![1], 1, 0, 0),
            (vec![1], 2, -1, -1),
            (vec![1, 2], 2, 1, 1),
            (vec![2, 2], 3, -1, -1),
        ];
        for (sorted, target, expected_first, expected_last) in cases {
            let (first, last) = first_and_last_pos(&sorted, &target);
            assert_eq!(first, expected_first, "vec={sorted:?} target={target}");
            assert_eq!(last, expected_last, "vec={sorted:?} target={target}");
        }
    }

    #[test]
    fn test_trapping_rain_water() {
        let cases: Vec<(Vec<i32>, i32)> = vec![
            (vec![0,1,0,2,1,0,1,3,2,1,2,1], 6),
            (vec![4,2,0,3,2,5], 9),
        ];
        for (height, expected) in cases {
            let actual = trapping_rain_water(height.clone());
            assert_eq!(expected, actual, "{:?}", height);
        }
    }
}
