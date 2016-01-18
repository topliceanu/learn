#include <stdio.h>

int main(int argc, char *argv[]) {
  int i;

  char *states[] = {"California", "Texas", "Oregon", "Washington"};
  int num_states = 4;

  // print the arguments.
  puts("Print arguments:");
  i = argc - 1;
  while (i >= 0) {
    printf("arg %d: %s.\n", i, argv[i]);
    i -= 1;
  }

  // print the states.
  puts("Print states:");
  i = num_states - 1;
  while (i >= 0) {
    printf("state %d: %s.\n", i, states[i]);
    i -= 1;
  }

  // extra: copy argvs into states.
  i = 0;
  while (i < num_states || i < argc) {
    states[i] = argv[i];
    i += 1;
  }

  // print the states.
  puts("Print copied arguments:");
  i = 0;
  while (i < num_states) {
    printf("state %d: %s.\n", i, states[i]);
    i += 1;
  }

  return 0;
}
