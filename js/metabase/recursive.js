/* Making Change
Given a number "x" and a sorted array of coins "coinset", write a function
that returns the amounts for each coin in the coinset that sums up to X or
indicate an error if there is no way to make change for that x with the given
coinset. For example, with x=7 and a coinset of [1,5,10,25], a valid answer
would be {1: 7} or {1: 2, 5: 1}. With x = 3 and a coinset of [2,4] it should
indicate an error. Bonus points for optimality.

Use the following examples to test it out

A. x = 6 coinset = [1,5,10,25]
B. x = 6, coinset = [3,4]
C. x = 6, coinset = [1,3,4]
D. x = 6, coinset = [5,7]
*/

// TESTS

console.log(makeChange(6, [1,5,10,25]))
console.log(makeChange(6, [3,4]))
console.log(makeChange(6, [1,3,4]))
console.log(makeChange(6, [5,7]))

// EXTRA TESTS

console.log(makeChange(5, [7, 8]))
console.log(makeChange(5, [6, -1])) // This broke the stack because instead of reducing the branching, it increases it.
console.log(makeChange(-1, [1, 2, 3]))
console.log(makeChange(0, [0, 1, 2])) // This broke the stack because it increased the branches to try.
console.log(makeChange(0, [1, 2])) // This accepted the empty solution.
console.log(makeChange(1111, [1, 5, 10, 25])) // This is the max number of zeros before the stack broke.
console.log(makeChange(6, []))

// @return {String}
function makeChange(x, coinSet) {
  if (x <= 0 || coinSet.some(c => c <= 0)) {
    return `x has to be larger than 0 and all values in coinSet have to be larger than 0`;
  }
  const [isSolution, solution] = solve([], x, coinSet.reverse());
  if (!isSolution) {
    return `Unable to find exact change for x=${x} and coinSet=${coinSet}`;
  }
  return `Change is ${solution}`;
}

// @param {Array<Number>} solution
// @param {Number} sum
// @param {Array<Number>} coinSet
// @return (Boolean, Array<Number>)
function solve(solution, sum, coinSet) {
  if (isSolution(solution, sum)) {
    return [true, solution];
  }
  if (!canExtendSolution(solution, sum, coinSet)) {
    return [false, solution];
  }
  const extensions = coinSet.map(coin => appendCoin(solution, coin));
  for (let i = 0; i < extensions.length; i ++) {
    const extension = extensions[i];
    const [isSolution, newSolution] = solve(extension, sum, coinSet);
    if (isSolution) {
      return [isSolution, newSolution];
    }
  }
  return [false, solution];
}

function isSolution(candidate, sum) {
  return sum === candidate.reduce((s, c) => s + c, 0);
}

function canExtendSolution(candidate, sum, coinSet) {
  // TODO optimise this
  return sum > candidate.reduce((s, c) => s + c, 0);
}

function appendCoin(candidate, coin) {
  const newCandidate = candidate.slice();
  newCandidate.push(coin);
  return newCandidate;
}
