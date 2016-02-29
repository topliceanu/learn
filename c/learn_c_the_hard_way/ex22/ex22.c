#include "ex22.h"
#include "../dbg.h"

// THE_SIZE is defined in ex22.h as `extern` so it's the same variable.
int THE_SIZE = 1000;

// THE_AGE is not visible outside this file.
static int THE_AGE = 29;

int get_age() {
  return THE_AGE;
}

void set_age(int age) {
  THE_AGE = age;
}

double update_ratio(double new_ratio) {
  static double ratio = 1.0;

  double old_ratio = ratio;
  ratio = new_ratio;

  return old_ratio;
}

void print_size() {
  log_info("I think size is: %d", THE_SIZE);
}
