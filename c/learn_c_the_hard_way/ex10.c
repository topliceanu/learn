#include <stdio.h>

int main(int argc, char *argv[]) {
  int i = 0;

  // Our own array of strings.
  char *states[] = {"California", "Oregon", "Washington", "Texas"};
  int num_states = 4;

  // extra: interchange a state with an argument.
  char *tmp = states[0];
  states[0] = argv[0];
  argv[0] = tmp;

  // Go through all params of the script and print them.
  // First item in argv is the name of the script!
  for (i = 0; i < argc; i++) {
    printf("arg %d: %s\n", i, argv[i]);
  }

  for (i = 0; i < num_states; i++) {
    printf("state %d: %s.\n", i, states[i]);
  }

  return 0;
}
