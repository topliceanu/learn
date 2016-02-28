#include <stdio.h>

#include "../minunit.h"
#include "min_heap.c"

#define print_r(arr) for(int i=0, n = sizeof(arr)/sizeof(int); i < n; i ++) { printf("%i, ", arr[i]); } printf("\n")

int tests_run = 0;

static char *test_left_child() {
  mu_assert("left child of 0 is 1", left_child(0) == 1);
  mu_assert("left child of 1 is 3", left_child(1) == 3);
  return 0;
}

static char *test_right_child() {
  mu_assert("right child of 0 is 2", right_child(0) == 2);
  mu_assert("right child of 1 is 4", right_child(1) == 4);
  return 0;
}

static char *test_inter_change() {
  int subject[] = {1, 2, 3, 4, 5};
  int result = inter_change(&subject, 1, 2);
  int expected[] = {1, 3, 2, 4, 5};

  print_r(subject);
  print_r(expected);
  mu_assert("interchange switched two valid positions", subject == expected);
  mu_assert("interchange return success", result == 0);

  result = inter_change(&subject, 0, 6);
  mu_assert("interchange returned out of bounds error", result == 1);
  mu_assert("interchange didn't modify the array", subject[1] == 3);
  return 0;
}

static char *all_tests() {
  mu_run_test(test_left_child);
  mu_run_test(test_right_child);
  mu_run_test(test_inter_change);
  return 0;
}

int main (int argc, char *argv[]) {
  char *result = all_tests();
  if (result != 0) {
    printf("Test failed: %s\n", result);
  }
  else {
    printf("All tests have passed!\n");
  }
  printf("Number of tests run %d\n", tests_run);
  return result != 0;
}
