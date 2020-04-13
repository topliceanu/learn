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

class Backtracking {
  constructor(sum, coinSet) {
    this.sum = sum;
    this.coinSet = coinSet.filter(c => c <= sum).reverse();;
    this.solutions = [];
  }

  // Executes the backtracking algorithm and returns the results
  run() {
    if (this.sum < 0 || this.coinSet.some(c => c <= 0)) {
      return
    }
    const seed = this.root();
    this.recurrence(seed);
  }

  // Main recurrence of the algorithm.
  // Returns the first valid solution.
  recurrence(candidate) {
    if (!this.shouldContinue(candidate)) {
      return;
    }
    if (this.reject(candidate)) {
      return;
    }
    if (this.accept(candidate)) {
      this.output(candidate);
    }
    const solutions = this.extend(candidate);
    solutions.forEach(solution => {
      this.recurrence(solution);
    });
  }

  // Return the partial candidate at the root of the search tree, ie. the seed!
  root() {
    return [];
  }

  // Hook to allow implementation to stop the algorithm early.
  // Defaults to True, meaning explore the entire solutions space.
  shouldContinue(candidate) {
    return sum(candidate) <= this.sum;
  }

  // Returns true if the candidate is a valid final solution.
  accept(candidate) {
    return candidate.length > 0 && sum(candidate) === this.sum;
  }

  // Returns true only if the candidate cannot possibly form a correct.
  reject(candidate) {
    sum(candidate) > this.sum;
  }

  // Extends the of the given candidate partial solution.
  extend(candidate) {
    return this.coinSet.map(coin => {
      const newCandidate = candidate.slice();
      newCandidate.push(coin);
      return newCandidate;
    });
  }

  // When a solutions is found, it is recorded.
  output(solution) {
    this.solutions.push(solution);
  }
}

// HELPERS

function sum(partial) {
  return partial.reduce((acc, p) => acc + p, 0);
}

function makeChange(x, coinSet) {
  const bt = new Backtracking(x, coinSet);
  bt.run();
  if (bt.solutions.length === 0) {
    return `Unable to produce exact change for x=${x} and coinSet=${coinSet}.`;
  }
  return `Change is ${bt.solutions[0]}.`;
}

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
console.log(makeChange(1000, [1])) // This is the max number of zeros before the stack broke.
console.log(makeChange(6, []))
