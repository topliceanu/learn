#include "ex22.h"
#include "../dbg.h"

const char *MY_NAME = "Alex Topliceanu";


void scope_demo(int count) {
  log_info("Count is: %d", count);

  if (count > 10) {
    int count = 100; // you can shaddow a variable.

    log_info("count in this scope is %d", count);
  }
  log_info("count is at exit: %d", count);

  count = 3000;
  log_info("count after assign: %d", count);
}

int main(int argc, char *argv[]) {
  // prints name = Alex Toliceanu and age = 29
  log_info("My name: %s, age: %d", MY_NAME, get_age());

  set_age(100);
  // Prints age = 1000
  log_info("My age is now: %d", get_age());

  // prints THE_SIZE = 1000 because THE_SIZE is set as extern.
  log_info("THE_SIZE is: %d", THE_SIZE);
  print_size(); // prints THE_SIZE=1000

  THE_SIZE = 9;

  // prints THE_SIZE = 9 again, because THE_SIZE is extern.
  log_info("THE_SIZE is: %d", THE_SIZE);
  print_size(); // print

  // test the ratio function static.
  log_info("Ratio at first is: %f", update_ratio(2.0));
  log_info("Ratio again: %f", update_ratio(10.0));
  log_info("Ratio once more: %f", udpate_ratio(300.0));

  // thest the scope demo
  int count = 4;
  scope_demo(count);
  scope_demo(count * 20);

  log_info("Count after calling scope_demo: %d", count);
  return 0;
}
