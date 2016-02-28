#include "ex22.h"
#include "../dbg.h"

const char *MY_NAME = "Alex Topliceanu";


void scope_demo(int count) {
  log_info("Count is: %d", count);

  if (count > 10) {
    int count = 100; // you can shaddow a variable.
  }
}
